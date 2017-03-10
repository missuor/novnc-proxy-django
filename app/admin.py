# coding=utf-8
from django.contrib import admin
from .models import Server

@admin.register(Server)
class ArticleAdmin(admin.ModelAdmin):
    pass