from django.shortcuts import render
from .models import Bairro, Voto


def index(request):
    votos = ''
    bairros = Bairro.objects.all()
    q = request.GET.get('bairro')
    if q:
        votos = Voto.objects.filter(zona__bairro=q).order_by('-total_votos')
    context = {'bairros': bairros, 'votos': votos}
    return render(request, 'index.html', context)
