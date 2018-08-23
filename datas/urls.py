from django.conf.urls import url
from datas.views import adicionar, lista

urlpatterns = [
    url(r'^$', lista, name="lista"),
    url(r'^adicionar/', adicionar, name="adicionar"),
]