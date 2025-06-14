from django.db import models
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
class Product(models.Model):
    title =  models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="reviews", on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review for {self.product.title}"


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reviews/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)

            max_size = (800, 800)
            img.thumbnail(max_size)

            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=85, optimize=True)
            image_content = ContentFile(buffer.getvalue())

            self.image.save(self.image.name, image_content, save=False)

        super().save(*args, **kwargs)
    def __str__(self):
        return f"Image for {self.review.product.title} by {self.review.user.username}"

