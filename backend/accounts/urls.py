from django.contrib import admin
from django.urls import path,include
from . views import LogoutView,CustomLoginView,CurrentUserView
urlpatterns = [
    path('login/',CustomLoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('user/',CurrentUserView.as_view()),
    # path('google/', GoogleLoginView.as_view()),

    
]