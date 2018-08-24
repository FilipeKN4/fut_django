from django.conf.urls import url
from contas.views import login_usuario, registrar, sair

urlpatterns = [
    url(r'^$', login_usuario, name='login'),
    url(r'^registro/', registrar, name='registrar'),
    url(r'^sair/', sair, name='sair'),
]