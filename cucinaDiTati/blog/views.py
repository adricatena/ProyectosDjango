from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.


def blog(request):
    posteos = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'blog/blog.html', {'posteos': posteos})
