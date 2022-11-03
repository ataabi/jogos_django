from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.models import User


# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    if request.method == 'POST':
        nick = request.POST['u_nick']
        nome = request.POST['u_name']
        senha = request.POST['u_senha']
        email = request.POST['u_email']

        novo_usuario = User.objects.create_user(
            username=nick, first_name=nome,
            password=senha, email=email)
        novo_usuario.save()
        
        return redirect('login')

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'login.html')

    if request.method == 'POST':
        nome = request.POST['u_name']
        senha = request.POST['u_senha']
        usuario = authenticate(username=nome, password=senha)
        if usuario is not None:
            user_login(request, usuario)
            return redirect('index')
        else:
            return redirect('login')

        
def logout(request):
    user_logout(request)
    return redirect('index')