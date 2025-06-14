from rest_framework import serializers
from . models import ReviewImage,Review
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ["image"]

    def validate_image(self,value):
        # open the image from inmemory uploaded file 
        img = Image.open(value)

        max_size = (800,800)
        img.thumbnail(max_size)

        buffer =BytesIO()
        img.save(buffer, format='jpeg',quality=85,optimize=True)

        # replace original upload image with optimized version
        value = ContentFile(buffer.getvalue(),name=value.name)

        return value
    
class ReviewSerializer(serializers.ModelSerializer):
    images = ReviewImageSerializer(many=True, write_only=True)

    class Meta:
        model = Review
        fields = ['product', 'caption', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        review = Review.objects.create(**validated_data)
        for image_data in images_data:
            ReviewImage.objects.create(review=review, image=image_data['image'])
        return review

            