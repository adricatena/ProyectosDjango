from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.


def blog(request):
    posteos = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'blog/blog.html', {'posteos': posteos, 'categorias': categorias})


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posteos = Post.objects.filter(categorias=categoria)
    return render(request, 'blog/categoria.html', {'categoria': categoria, 'posteos': posteos})
