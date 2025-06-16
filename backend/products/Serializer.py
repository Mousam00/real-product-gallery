from rest_framework import serializers
from . models import ReviewImage,Review
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

from rest_framework import serializers
from .models import Product, Review, ReviewImage

class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ['image']

class ReviewSerializer(serializers.ModelSerializer):
    images = ReviewImageSerializer(many=True, read_only=True)
    uploaded_images = ReviewImageSerializer(many=True, write_only=True)
    user = serializers.StringRelatedField(read_only=True)
    product_url = serializers.URLField(write_only=True)
    product_title = serializers.CharField(write_only=True)
    product_description = serializers.CharField(write_only = True, required=False)

    class Meta:
        model = Review
        fields = ['id', 'product_url', 'product_title', 'product_description', 'caption','images', 'uploaded_images', 'user', 'created_at']

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images')
        url = validated_data.pop('product_url')
        title =validated_data.pop('product_title')
        description = validated_data.pop('product_description')


        product , created = Product.objects.get_or_create(url=url,defaults={'title':title,'description' :description})
        review = Review.objects.create(product=product,user=self.context['request'].user,caption=validated_data.get('caption'))


        for image_file in images_data:
            ReviewImage.objects.create(review=review, image=image_file)
        
        return review

