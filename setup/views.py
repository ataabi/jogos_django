from django.shortcuts import render
from usuarios.models import Ranking


def index(request):
    ranking_pergunta = Ranking.objects.all().order_by('-pontos_pergunta')
    ranking_forca = Ranking.objects.all().order_by('-pontos_forca')

    contexto = {
        'ranking_pergunta':ranking_pergunta,
        'ranking_forca':ranking_forca,
    }

    return render(request, 'index.html', contexto)