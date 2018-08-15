from django.conf.urls import url
from liga.views import index, adicionar, mostrar, editar, excluir

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^novo_time/', adicionar, name='adicionar'),
    url(r'^time/(?P<id>\d+)/$', mostrar, name='mostrar'),
    url(r'^editar/(?P<id>\d+)/$', editar, name='editar'),
    url(r'^time/(?P<id>\d+)/excluir/$', excluir, name='excluir'),
]