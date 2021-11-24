from django.contrib import admin
from django.contrib.auth import models
from django.db.models import fields
from .models import User
# Register your models here.

from django.contrib.auth.admin import UserAdmin

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    # fieldsets = UserAdmin.fieldsets +
    fieldsets = (
        ('User Profile', {
            "fields": (
                'photo',
                'photo_thumbnail'
            ),
        }),
    )
    
admin.site.register(User, CustomUserAdmin)

        # (
        #     (
        #         'User Profile',
        #         {
        #             'fields' : (
        #                 'photo'
        #             ),
        #         },
        #     ),
        # )
    