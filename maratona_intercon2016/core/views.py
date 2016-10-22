from django.shortcuts import render
from .models import Bairro


def index(request):
    bairros = Bairro.objects.all()
    context = {'bairros': bairros}
    return render(request, 'index.html', context)
