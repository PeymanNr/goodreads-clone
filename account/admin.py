from django.contrib import admin
from django.contrib.admin import register
from account.models import MyUser


@register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')