from django.shortcuts import render
from django.views import generic
from .models import blog_author, blog, blog_comment

# Create your views here.
def index(request):
    return render(request, 'index.html')

class BlogListWiew(generic.ListView):
    model = blog

class AuthorListWiew(generic.ListView):
    model = blog_author

class BlogDetailView(generic.DetailView):
    model = blog

class BlogAuthorDetailView(generic.DeleteView):
    model = blog_author