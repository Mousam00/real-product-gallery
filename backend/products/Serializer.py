from rest_framework import serializers
from .models import Product, Review, ReviewImage
from django.db.models import Avg
from .utils import get_resized_image_url


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    submited_by = serializers.StringRelatedField(source='submited_by.username', read_only=True)
    submited_at = serializers.DateTimeField(source='created_at', format='%Y-%m-%d', read_only=True)
    initialReview = serializers.SerializerMethodField()
    first_image = serializers.SerializerMethodField()
    all_reviews = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'url', 'description', 'status', 'first_image',
            'average_rating', 'submited_by', 'submited_at', 'initialReview', 'all_reviews'
        ]
        read_only_fields = ['status', 'submited_by', 'created_at']

    def get_initialReview(self, obj):
        review = obj.reviews.first()
        return ReviewSummarySerializer(review).data if review else None

    def get_first_image(self, obj):
        first_image = ReviewImage.objects.filter(review__product=obj).first()
        if first_image:
            return get_resized_image_url(first_image.image, width=600, height=600)
        return None


    def get_all_reviews(self, obj):
        all_reviews = Review.objects.filter(product=obj).order_by('-created_at')
        return ReviewSerializer(all_reviews, many=True).data

    def get_average_rating(self, obj):
        return round(obj.reviews.aggregate(avg=Avg('rating'))['avg'] or 0, 1)


class ReviewSerializer(serializers.ModelSerializer):
    images = ReviewImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True
    )
    user = serializers.StringRelatedField(read_only=True)

    product_url = serializers.URLField(write_only=True)
    product_title = serializers.CharField(write_only=True)
    product_description = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Review
        fields = [
            'id', 'product_url', 'product_title', 'product_description',
            'caption', 'images', 'uploaded_images', 'user', 'rating', 'created_at'
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images')
        product_url = validated_data.pop('product_url')
        product_title = validated_data.pop('product_title')
        product_description = validated_data.pop('product_description', '')
        user = self.context['request'].user

        product, _ = Product.objects.get_or_create(
            url=product_url,
            defaults={
                'title': product_title,
                'description': product_description,
                'submited_by': user
            }
        )

        review = Review.objects.create(
            product=product,
            user=user,
            caption=validated_data.get('caption'),
            rating=validated_data.get('rating', 0)
        )

        self._save_review_images(images_data, review)

        return review

    def _save_review_images(self, images_data, review):
        for image_file in images_data:
            image_instance = ReviewImage(review=review)
            image_instance.image.save(image_file.name, image_file, save=True)


class OnlyReviewSerializer(serializers.ModelSerializer):
    images = ReviewImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True
    )
    user = serializers.StringRelatedField(read_only=True)

    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'product', 'caption', 'images', 'uploaded_images',
            'user', 'rating', 'created_at'
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images')
        product = validated_data.pop('product')
        user = self.context['request'].user

        review = Review.objects.create(
            product=product,
            user=user,
            caption=validated_data.get('caption'),
            rating=validated_data.get('rating', 0)
        )

        self._save_review_images(images_data, review)

        return review

    def _save_review_images(self, images_data, review):
        for image_file in images_data:
            image_instance = ReviewImage(review=review)
            image_instance.image.save(image_file.name, image_file, save=True)


class ReviewSummarySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.username', read_only=True)
    images = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'caption', 'rating', 'images', 'created_at']

    def get_images(self, obj):
        return [
            get_resized_image_url(img.image, 800, 800)
            for img in obj.images.all()
        ]


class FeaturedProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    featured_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'average_rating', 'featured_image']

    def get_average_rating(self, obj):
        return round(obj.reviews.aggregate(avg=Avg('rating'))['avg'] or 0, 1)

    def get_featured_image(self, obj):
        first_image = ReviewImage.objects.filter(review__product=obj).first()
        if first_image:
            return get_resized_image_url(first_image.image, 600, 600)
        return None
