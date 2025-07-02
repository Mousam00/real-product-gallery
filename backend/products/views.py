from django.shortcuts import render
from rest_framework import viewsets,permissions
from . Serializer import ReviewSerializer,OnlyReviewSerializer
from . models import Review
from .Serializer import ProductSerializer
from .Serializer import FeaturedProductSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Product
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
    queryset =Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the review
        serializer.save(user=self.request.user)

class OnlyReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = OnlyReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeaturedProductsView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.filter(status='approved')
    serializer_class = FeaturedProductSerializer

class ProductDetailsView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class GalleryView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.filter(status='approved')
    serializer_class = ProductSerializer
    
class AdminPanelView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Product.objects.filter(status='pending')
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        product = self.get_object()
        product.status = 'approved'
        product.save()
        return Response({'status': 'product approved'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        product = self.get_object()
        product.status = 'rejected'
        product.save()
        return Response({'status': 'product rejected'}, status=status.HTTP_200_OK)
