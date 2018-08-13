from django.shortcuts import render
from liga.forms import TimeForm, TimeModelForm

from .models import Time

# Create your views here.
def index(request):
    times = Time.objects.all()

    context = {
        "times": times,
    }

    return render(request, "liga/index.html", context)

def adicionar(request):
    time_form = TimeModelForm(request.POST or None)

    if time_form.is_valid():
        time_form.save()
        #time_dados = time_form.cleaned_data
        #nome = time_dados.get("nome")
        #sigla_estado = time_dados.get("sigla_estado")
        #time = Time.objects.create(nome=nome, sigla_estado = sigla_estado)

    context = {
        "form" : time_form,
    }

    return render(request, "novo_time.html", context)