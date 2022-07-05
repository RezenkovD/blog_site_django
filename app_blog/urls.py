from django.urls import path

from . import views

urlpatterns = [
   path('blog/', views.index, name='index'),
   path('blog/blogs/', views.BlogListWiew.as_view(), name='blogs'),
   path('blog/blog_authors/', views.AuthorListWiew.as_view(), name='blog_authors'),
   path('blog/blogs/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
   path('blog/blog_authors/<int:pk>', views.BlogAuthorDetailView.as_view(), name='author-detail'),
]