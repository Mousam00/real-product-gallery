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
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True
    )
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'product', 'caption', 'images', 'uploaded_images', 'user', 'created_at']

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images')
        review = Review.objects.create(**validated_data)
    
        for image_file in images_data:
            ReviewImage.objects.create(review=review, image=image_file)
        
        return review

