from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from .models import Pergunta
from usuarios.models import Ranking

from random import shuffle

# Create your views here.


def perguntas(request):

    if request.method == 'GET':
        pergunta = Pergunta.objects.all().order_by('?')[0]
        request.session['lista_perguntas'] = []
        return render(request, 'perguntas.html', {'pergunta':pergunta})

    if request.method == 'POST':

        # Pegando o PID(ID da pergunta)
        pid = int(request.POST['pid'])

        #Verifica se a lista de perguntas respondidas contem o ID da pergunta
        if pid in request.session['lista_perguntas']:
            #Pegando as perguntas do banco de forma aleatoria 
            perguntas = Pergunta.objects.all().order_by('?')
            
            # Procurando uma pergunta que nao exista dentro da lista
            for p in perguntas:
                print('PERGUNTAS GERADAS', p)
                if int(p.id) not in request.session['lista_perguntas']:
                    pergunta = p
                    break
        else:
            pergunta = Pergunta.objects.get(pk=pid)

        # Limpa a lista de perguntas respondidas caso ela exceda o valor de 10 itens
        if len(request.session['lista_perguntas']) >= 10:
            request.session['lista_perguntas'].clear()

        # Adicionando o ID da pergunta na lista de perguntas
        request.session['lista_perguntas'].append(pergunta.id)
   
        # Criando o dicionario de contexto
        contexto = {'pergunta':pergunta}

        #verifica se a resposta do cliente é iqual a do servidor
        if 'resposta' in request.POST:
            #Pegando a resposta do cliente para comparando com a do servidor
            resposta_cliente = request.POST['resposta']
            pergunta_servidor = Pergunta.objects.get(pk=request.POST['pid'])

            # Verificando se o cliente está logado 
            if request.user.is_authenticated:

                nome_usuario = request.user
                print('RESQUET USER = ', nome_usuario)
                # Tentando pegar os pontos do cliente em caso de falha adiciona ele no ranking
                try:
                    user_ranking = Ranking.objects.get(pk=nome_usuario)
                    print('normal')
                except:
                    print('except')
                    user_ranking = Ranking(user=nome_usuario)

                print('PONTOS PERGUNTAS : ',user_ranking.pontos_pergunta,'\n')
                # Comparando as respostas e adicionando ou removendo os pontos do cliente
                if resposta_cliente == pergunta_servidor.resposta:
                    contexto['confirmacao'] = 'correto'
                    user_ranking.pontos_pergunta += 1
                else:
                    contexto['confirmacao'] = 'errado'
                    user_ranking.pontos_pergunta -= 1
                    

                # Criando a na sessão a variavel pontos 
                user_ranking.save()  
                request.session['pontos'] = user_ranking.pontos_pergunta
                    
            else:
                print('USUARIO NÂO LOGADO')
                if resposta_cliente == pergunta_servidor.resposta:
                    contexto['confirmacao'] = 'correto'
                else:
                    contexto['confirmacao'] = 'errado'
            
            contexto['resposta_cliente'] = resposta_cliente

    return render(request, 'perguntas.html', contexto)


    
