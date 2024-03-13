from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('estudiante/', estudiante_form, name='estudiante_form'),
    path('profesor/', profesor_form, name='profesor_form'),
    path('curso/', curso_form, name='curso_form'),
    path('camada/', camada_search, name='camada_search'),


]