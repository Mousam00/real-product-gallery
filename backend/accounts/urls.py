from django.contrib import admin
from django.urls import path,include
from . views import LogoutView,CustomLoginView
urlpatterns = [
    path('login/',CustomLoginView.as_view()),
    path('logout/',LogoutView.as_view())
]