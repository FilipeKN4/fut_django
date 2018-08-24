from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.

def redirect_root(request):
    return HttpResponseRedirect('/login/')

def login_usuario(request):
    print(request.user.is_authenticated())
    titulo = "Login"
    form = UserLoginForm(request.POST or None)
    
    if form.is_valid():
        nome_usuario = form.cleaned_data.get("nome_usuario")
        senha = form.cleaned_data.get("senha")
        usuario = authenticate(username=nome_usuario, password=senha)
        login(request, usuario)
        print(request.user.is_authenticated())
        return HttpResponseRedirect('/times/')

    context = {
        "form": form,
        "titulo": titulo,
    }

    return render(request, "login.html", context)

def registrar(request):
    print(request.user.is_authenticated())
    titulo = "Registrar"
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        usuario = form.save(commit=False)
        senha = form.cleaned_data.get('senha')
        usuario.set_password(senha)
        usuario.save()
        novo_usuario = authenticate(username=usuario, password=senha)
        login(request, novo_usuario)
        return HttpResponseRedirect('/times/')

    context = {
        "form" : form,
        "titulo" : titulo,
    }

    return render(request, "registrar.html", context)

def sair(request):
    logout(request)
    return HttpResponseRedirect('/login/')