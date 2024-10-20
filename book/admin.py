from django.contrib import admin
from django.contrib.admin import register
from book.models import Book, Comment, Rating


# Register your models here.

@register(Book)
class BookAmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bookmark_count')

@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'user', 'text')

@register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'user', 'rating')
