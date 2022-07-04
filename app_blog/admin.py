from django.contrib import admin
from .models import blog_author, blog, blog_comment

# Register your models here.

admin.site.register(blog)
admin.site.register(blog_author)
admin.site.register(blog_comment)