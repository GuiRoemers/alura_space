from django.urls import path
from galeria.views import *


urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    path('mais_vistas/', mais_vistas, name='mais_vistas'),
    path('novas/', novas, name='novas'),
    path('surpreenda_me/', surpreenda_me, name='surpreenda_me'),
]
