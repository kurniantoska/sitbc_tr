from django.contrib import admin
from . models import (
    Board, Topic, Post
)


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ('name',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
