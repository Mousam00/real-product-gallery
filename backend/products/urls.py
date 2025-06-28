from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet
from .views import FeaturedProductsView,ProductDetailsView,GalleryView
from .views import AdminPanelView
router = DefaultRouter()

router.register(r'review',ReviewViewSet,basename='review')
router.register(r'admin',AdminPanelView,basename='product')
# router.register(r'featured',FeaturedProductsView,basename='featured')

urlpatterns = [
    path('', include(router.urls)),
    path('featured/', FeaturedProductsView.as_view(), name='featured-products'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product-details'),

]