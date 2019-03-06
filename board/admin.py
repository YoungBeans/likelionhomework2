from django.contrib import admin
from .models import Post
# Register your models here.

class BoardList(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    list_display_links = ['title']

admin.site.register(Post, BoardList)