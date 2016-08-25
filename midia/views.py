from django.shortcuts import render, get_object_or_404


# Create your views here.
from midia.models import Filme, Diretor, Ator


def filme_detail(request, id):
    filme = get_object_or_404(Filme, pk=id)
    context = {'filme': filme}
    return render(request, 'midia_detail.html', context)

def index(request):
    return render(request, 'home.html', {})

def atores_list(request):
    atores = Ator.objects.all()
    context = {'atores': atores}
    return render(request, 'atores_list.html', context)

def filmes_list(request):
    filmes = Filme.objects.all()
    context = {'filmes': filmes}
    return render(request, 'filmes_list.html', context)

def diretores_list(request):
    diretores = Diretor.objects.all()
    context = {'diretores': diretores}
    return render(request, 'diretores_list.html', context)