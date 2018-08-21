from django.conf.urls import url
from contas.views import login_usuario, registrar

urlpatterns = [
    url(r'^$', login_usuario, name='login'),
    url(r'^registro/', registrar, name='registrar'),
]