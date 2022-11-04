from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from .models import Pergunta, RankingPergunta

from random import shuffle

# Create your views here.

def index(request):
    return render(request, 'index.html')

def perguntas(request):

    if request.method == 'GET':
        pergunta = Pergunta.objects.all().order_by('?')[0]
        request.session['lista_perguntas'] = []

        return render(request, 'perguntas.html', {'pergunta':pergunta})


    

    if request.method == 'POST':
    # Verifica se a resposta esta correta
        if 'pid' in request.POST:
            pid = int(request.POST['pid'])

            #verifica se a lista de perguntas respondidas ja foi criada
            if 'lista_perguntas' in request.session:
                
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

            else:
                # Cria a lista de perguntas e devolve a mesma pergunta caso a lista ainda nao exista
                request.session['lista_perguntas'] = []
                pergunta = Pergunta.objects.get(pk=pid)

        # Adicionando o ID da pergunta na lista de perguntas
        request.session['lista_perguntas'].append(pergunta.id)
   
        # Criando o dicionario de contexto
        contexto = {
            'pergunta':pergunta
        }

        #verifica se a resposta do cliente é iqual a do servidor
        if 'resposta' in request.POST:
            resposta_cliente = request.POST['resposta']
            pergunta_servidor = Pergunta.objects.get(pk=request.POST['pid'])

            if request.user.is_authenticated:
                print('USUARIO LOGADO')
                print(request.user.username)
                nome_usuario = request.user
                try:
                    user_ranking = RankingPergunta.objects.get(pk=nome_usuario)
                except:
                    user_ranking = RankingPergunta(user=nome_usuario, pontos_pergunta=0)
                    
            else:
                print('USUARIO NÂO LOGADO')

            if resposta_cliente == pergunta_servidor.resposta:
                contexto['confirmacao'] = 'correto'
                user_ranking.pontos_pergunta += 1
            else:
                contexto['confirmacao'] = 'errado'
                user_ranking.pontos_pergunta -= 1

            request.session['pontos'] = user_ranking.pontos_pergunta
                

            user_ranking.save()
            
            contexto['resposta_cliente'] = resposta_cliente

    return render(request, 'perguntas.html', contexto)


    
