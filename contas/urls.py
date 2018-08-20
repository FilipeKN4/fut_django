from django.conf.urls import url
from contas.views import login_usuario

urlpatterns = [
    url(r'^$', login_usuario, name='login'),
]