from django.urls import path

from . import views

urlpatterns = [
   path('blog/', views.index, name='index'),
   path('blog/blogs/', views.BlogListWiew.as_view(), name='blogs'),
   path('blog/bloggers/', views.AuthorListWiew.as_view(), name='authors'),
   path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
   path('blog/blogger/<int:pk>', views.BlogAuthorDetailView.as_view(), name='author-detail'),
]