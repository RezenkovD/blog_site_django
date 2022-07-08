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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

class blogcreate(PermissionRequiredMixin, CreateView):
    permission_required = 'app_blog.add_blog'    
    model = blog
    fields = '__all__'

class blogdelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'app_blog.delete_blog'
    model = blog
    success_url = reverse_lazy('blogs')

class blogupdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_blog.change_blog'
    model = blog
    fields = '__all__'
    
class authorcreate(PermissionRequiredMixin, CreateView):
    permission_required = 'app_blog.add_blog_author'
    model = blog_author
    fields = '__all__'

class authordelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'app_blog.delete_blog_author'
    model = blog_author
    success_url = reverse_lazy('authors')

class authorupdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_blog.change_blog_author'
    model = blog_author
    fields = '__all__'

from django.urls import reverse

class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = blog_comment
    fields = ['blog', 'description']
        
    def get_success_url(self): 
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})
