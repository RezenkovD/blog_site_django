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

class blogcreate(LoginRequiredMixin, CreateView):
    model = blog
    fields = '__all__'

class blogdelete(LoginRequiredMixin, DeleteView):
    model = blog
    success_url = reverse_lazy('blogs')

class blogupdate(LoginRequiredMixin, UpdateView):
    model = blog
    fields = '__all__'
    
class authorcreate(LoginRequiredMixin, CreateView):
    model = blog_author
    fields = '__all__'

class authordelete(LoginRequiredMixin, DeleteView):
    model = blog_author
    success_url = reverse_lazy('authors')

class authorupdate(LoginRequiredMixin, UpdateView):
    model = blog_author
    fields = '__all__'

from django.urls import reverse


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = blog_comment
    fields = ['blog', 'description']
        
    def form_valid(self, form):
        form.instance.blog_author = self.request.user
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})
