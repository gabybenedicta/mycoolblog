from django.contrib import admin

# Register your models here.
from .models import Category , Post, User , Comment

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)