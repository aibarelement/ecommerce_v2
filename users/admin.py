from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(models.User, CustomUserAdmin)
