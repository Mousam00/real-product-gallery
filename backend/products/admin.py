from django.contrib import admin
from . models import Product,Review,ReviewImage
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    search_fields = ('title', 'url')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'created_at')
    search_fields = ('product__title', 'user__username')

admin.site.register(ReviewImage)