from django.shortcuts import render
from rest_framework import viewsets,permissions
from . Serializer import ReviewSerializer
from . models import Review
# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
    queryset =Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the review
        serializer.save(user=self.request.user)