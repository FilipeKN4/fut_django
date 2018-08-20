from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.
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

    context = {
        "form": form,
        "titulo": titulo,
    }

    return render(request, "login.html", context)

def registrar(request):
    titulo = "Registrar"
    form = UserRegisterForm(request.POST or None)

    context = {
        "form" : form,
        "titulo" : titulo,
    }
    return

def logout(request):
    return