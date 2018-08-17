from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from liga.forms import TimeForm, TimeModelForm

from .models import Time

# Create your views here.
def redirect_root(request):
    return HttpResponseRedirect('/times/')

def index(request):
    times = Time.objects.all()

    context = {
        "times": times,
    }

    return render(request, "index.html", context)

def adicionar(request):
    time_form = TimeModelForm(request.POST or None)

    if time_form.is_valid():
        time_form.save()

    context = {
        "form" : time_form,
    }

    return render(request, "novo_time.html", context)

def mostrar(request, id=None):
    time = get_object_or_404(Time, id=id)

    context = {
        "time": time,
    }

    return render(request, "time.html", context)

def editar(request, id=None):
    time = get_object_or_404(Time, id=id)
    time_form = TimeModelForm(request.POST or None, instance=time)

    if time_form.is_valid():
        time = time_form.save(commit=False)
        time.save()

    context = {
        "time": time,
        "form": time_form,
    }

    return render(request, "novo_time.html", context)

def excluir(request, id=None):
    time = get_object_or_404(Time, id=id)
    time.delete()
    return redirect("index")