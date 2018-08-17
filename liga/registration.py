from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render
from .forms import UserLoginForm

def login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        usuario = form.cleaned_data.get("usuario")
        senha = form.cleaned_data.get("senha")

    context = {
        "form": form,
    }

    return render(request, "login.html", context)

def registrar(request):
    return

def logout(request):
    return