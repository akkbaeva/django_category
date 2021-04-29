
from django.contrib import admin

# Register your models here.
from category.models import Category, Comment, TVShow

admin.site.register(Category)
admin.site.register(TVShow)
admin.site.register(Comment)