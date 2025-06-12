from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib import admin

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from django.contrib import messages
# Register your models here.
class UserAdmin(BaseUserAdmin):
    def blacklist_tokens_for_users(modeladmin, request, queryset):
        for user in queryset:
            tokens = OutstandingToken.objects.filter(user=user)
            for token in tokens:
                try:
                    token.blacklist()
                except Exception as e:
                    # token may already be blacklisted
                    pass
        messages.success(request, "Successfully blacklisted all tokens for selected users.")

    def delete_tokens_for_users(modeladmin, request, queryset):
        for user in queryset:
            OutstandingToken.objects.filter(user=user).delete()
        messages.success(request, "Successfully deleted all tokens for selected users.")
    # The forms to add and change user instances

    list_display = ["email", "username", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["username"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    readonly_fields=["created_at","updated_at"]
    filter_horizontal = []
    actions = [blacklist_tokens_for_users, delete_tokens_for_users]

# 
admin.site.register(User, UserAdmin)

