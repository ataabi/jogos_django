from django.shortcuts import render
from .models import Palavra
from usuarios.models import Ranking
from django.contrib.auth.models import User
from random import choice

# Create your views here.

def forca(request):
    # Verificando se a uma pagina a ser carregada caso nao aja inicie uma aleatoria 
    if not 'semente' in request.POST or 'proxima' in request.POST:
        
        #Gerando uma semente aleatoria com base nos ids
        lista_ids = [int(p.id) for p in Palavra.objects.all()]
        semente = choice(lista_ids)
        palavra = Palavra.objects.get(pk=semente)
        request.session['palavra_atual'] = palavra.palavra
        if 'lista_chutes' in request.session:
            request.session['lista_chutes'].clear()

    else:
        #Pegando uma semente da requisição POST e gerando a palavra
        semente = request.POST['semente']
        palavra = Palavra.objects.get(pk=semente)

    cor_do_botao = 'class="btn btn-secondary border border-dark" style="width:8%;"'
    
    contexto = {
        'palavra': palavra ,
        'cor_botao':cor_do_botao
    }   
    
    if request.method == 'POST':
        # Pegando o chute(letra) do cliente
        if 'chute' in request.POST:
            chute = request.POST['chute']
        else:
            chute = ''

        #Verificando se a lista de chutes ainda não foi criada
        if not 'lista_chutes' in request.session:
            lista = [chute]
            chances = 0
        else:    
            lista = request.session['lista_chutes'].copy()
            if not chute in lista:
                lista.append(chute)

            if request.POST['chances'].isnumeric():
                chances = int(request.POST['chances'])
            else:
                chances = 0

            if 'proxima' in request.POST:
                lista.clear()
                chances = 0
                
        request.session['lista_chutes'] = lista

        # Verifica se o chute esta correto 
        if chute in palavra.palavra:
            for letra in palavra.palavra:
                if chute == letra:
                    palavra_atualizada = request.session['palavra_atual'].replace(letra,'')
                    request.session['palavra_atual'] = palavra_atualizada
        else:
            chances += 1

        if request.user.is_authenticated:
            nome_usuario = request.user
            try:
                usuario = Ranking.objects.get(pk=nome_usuario)
            except:
                usuario = Ranking(user=nome_usuario)

            if len(request.session['palavra_atual']) == 0:
                contexto['confirmacao'] = 'vitoria'
                contexto['cor_botao'] = 'disabled class="btn btn-success border border-dark"'
                usuario.pontos_forca += 1
                
            elif chances >= 5:
                contexto['confirmacao'] = 'derrota'
                contexto['cor_botao'] = 'disabled class="btn btn-danger border border-dark"'
                usuario.pontos_forca -= 1

            usuario.save()

        else:
            if len(request.session['palavra_atual']) == 0:
                contexto['confirmacao'] = 'vitoria'
                contexto['cor_botao'] = 'disabled class="btn btn-success border border-dark"'
                
            elif chances >= 5:
                contexto['confirmacao'] = 'derrota'
                contexto['cor_botao'] = 'disabled class="btn btn-danger border border-dark"'

        contexto['chances'] = chances

    return render(request, 'forca.html', contexto)