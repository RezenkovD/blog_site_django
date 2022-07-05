from django.urls import path

from . import views

urlpatterns = [
   path('blog/', views.index, name='index'),
   path('blog/blogs/', views.BlogListWiew.as_view(), name='blogs'),
   path('blog/blog_authors/', views.AuthorListWiew.as_view(), name='blog_authors'),
]