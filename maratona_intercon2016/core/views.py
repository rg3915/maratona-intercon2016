from django.shortcuts import render
from .models import Bairro, Voto, Eleitor


def index(request):
    votos = ''
    eleitores = ''
    bairros = Bairro.objects.all()
    q = request.GET.get('bairro')
    if q:
        votos = Voto.objects.filter(zona__bairro=q).order_by('-total_votos')
        eleitores = Eleitor.objects.filter(zona__bairro=q).order_by('-qtd_eleitores_no_perfil')
    context = {'bairros': bairros, 'votos': votos, 'eleitores': eleitores}
    return render(request, 'index.html', context)
