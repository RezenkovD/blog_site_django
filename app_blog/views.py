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



#create/delete/update 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class blogcreate(CreateView):
    model = blog
    fields = '__all__'

class blogdelete(DeleteView):
    model = blog
    success_url = reverse_lazy('blogs')

class blogupdate(UpdateView):
    model = blog
    fields = '__all__'
    
class authorcreate(CreateView):
    model = blog_author
    fields = '__all__'

class authordelete(DeleteView):
    model = blog_author
    success_url = reverse_lazy('authors')

class authorupdate(UpdateView):
    model = blog_author
    fields = '__all__'