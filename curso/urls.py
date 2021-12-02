from django.conf.urls import url
from . import views

urlpatterns = [
    url('curso_lista/lista', views.curso_nueva, name ='curso_lista'),
    ]