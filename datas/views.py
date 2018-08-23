from django.shortcuts import render, redirect
from datetime import date

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
        print(data_form.cleaned_data.get("data"))
        datas = data_form.cleaned_data.get("data").split(',')
        print(datas)
        for data in datas:
            data_split_bar = data.split('/')

            data1 = int(data_split_bar[0])
            data2 = int(data_split_bar[1])
            data3 = int(data_split_bar[2])
            nova_data = date(year=data3, month=data1, day=data2)
            Data.objects.create(data=nova_data)
            print(nova_data)

        return redirect('lista')


    context = {
        "form" : data_form,
    }

    return render(request, "nova_data.html", context)