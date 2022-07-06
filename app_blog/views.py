from django.shortcuts import render
from django.views import generic
from .models import blog_author, blog, blog_comment
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

class BlogListWiew(generic.ListView):
    model = blog
    paginate_by = 5

class AuthorListWiew(generic.ListView):
    model = blog_author

class BlogDetailView(generic.DetailView):
    model = blog

class BlogAuthorDetailView(generic.DetailView):
    model = blog_author
    