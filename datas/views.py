from django.shortcuts import render, redirect

from .models import Data
from datas.forms import DataForm, DataModelForm

# Create your views here.
def lista(request):
    datas = Data.objects.all()

    context = {
        "datas": datas,
    }

    return render(request, "lista.html", context)

def adicionar(request):
    # datas = Data.objects.all()
    data_form = DataModelForm(request.POST or None)

    if data_form.is_valid():
        data_form.save()
        return redirect('lista')


    context = {
        "form" : data_form,
    }

    return render(request, "nova_data.html", context)