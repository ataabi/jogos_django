from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Pergunta

from random import shuffle

# Create your views here.

def index(request):
    return render(request, 'index.html')

def perguntas(request):

    # Paginação 

    # lista_randomizada = shuffle([p for p in Pergunta.objects.all()])

    paginator = Paginator(Pergunta.objects.all(), 1)
    page = request.GET.get('page')

    try:
        if 'pagina_atual' in request.POST:
            perguntas_por_pagina = paginator.page(request.POST['pagina_atual'])
        else:
            perguntas_por_pagina = paginator.page(page)
    except PageNotAnInteger:
        perguntas_por_pagina = paginator.page(1)
    except EmptyPage:
        perguntas_por_pagina = paginator(page(paginator.number))
  

    # Criando o dicionario de contexto
    contexto = {
        'perguntas':perguntas_por_pagina
        }

    if request.method == 'POST':

    # Verifica se a resposta esta correta
        #verifica se a resposta do cliente é iqual a do servidor
        if 'resposta' in request.POST:
            print('Teve uma resposta')
            resposta_cliente = request.POST['resposta']
            print('RESPOSTA DO CLIENTE',resposta_cliente)
            pergunta_servidor = Pergunta.objects.get(pk=request.POST['pid'])
            
            if not 'pontos' in request.session:
                request.session['pontos'] = 0

            # if 'pontos' in request.session:
            #         request.session['pontos'] = 0

            if resposta_cliente == pergunta_servidor.resposta:
                print('Confirmacao Correto')
                contexto['confirmacao'] = 'correto'
                request.session['pontos'] += 1
            else:
                print('Confirmacao Errado')
                contexto['confirmacao'] = 'errado'
                request.session['pontos'] -= 1
            
            print(resposta_cliente)
            contexto['resposta_cliente'] = resposta_cliente

            print('Pagina atual no post',request.POST['pagina_atual'])
            print('PONTOS :',request.session['pontos'])


    
    return render(request, 'perguntas.html', contexto)


    
