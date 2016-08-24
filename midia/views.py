from django.shortcuts import render, get_object_or_404


# Create your views here.
from midia.models import Filme


def filme_detail(request, id):
    filme = get_object_or_404(Filme, pk=id)
    context = {'filme': filme}
    return render(request, 'midia_detail.html', context)