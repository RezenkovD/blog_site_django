from django.urls import path

from . import views

urlpatterns = [
   path('blog/', views.index, name='index'),
   path('blog/blogs/', views.BlogListWiew.as_view(), name='blogs'),
   path('blog/bloggers/', views.AuthorListWiew.as_view(), name='authors'),
   path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
   path('blog/blogger/<int:pk>', views.BlogAuthorDetailView.as_view(), name='author-detail'),


    path('blog/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='blog_comment'),

]

urlpatterns += [
    path('blog/blogs/create/', views.blogcreate.as_view(), name='blog_create'),
    path('blog/<int:pk>/delete/', views.blogdelete.as_view(), name='blog_delete'),
    path('blog/<int:pk>/update/', views.blogupdate.as_view(), name='blog_update'),
]

urlpatterns += [
    path('blog/bloggers/create/', views.authorcreate.as_view(), name='author_create'),
    path('blog/blogger/<int:pk>/delete/', views.authordelete.as_view(), name='author_delete'),
    path('blog/blogger/<int:pk>/update/', views.authorupdate.as_view(), name='author_update'),
]