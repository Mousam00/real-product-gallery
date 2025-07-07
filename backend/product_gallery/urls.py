from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import GoogleAuthRedirectAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT redirect view - put this BEFORE the 'auth/' include paths
    path('auth/account/google/login/callback/', GoogleAuthRedirectAPIView.as_view(), name='google_auth_redirect'),

    # Auth
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    # Social login routes
    path('auth/social/', include('allauth.socialaccount.urls')),  # Connections, signup, cancelled, error etc
    path('auth/account/', include('allauth.urls')),  # <-- THIS is where /auth/login/google/ comes from

    # Accounts + Product APIs
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('products.urls')),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
