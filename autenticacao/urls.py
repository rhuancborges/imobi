from django.urls import path
from . import views 

 
urlpatterns = [
    # Cria a urls, chamando a função cadastro do view
    path('cadastro/', views.cadastro, name='cadastro'), 
    path('login/', views.login, name='login'),
    path('sair/', views.sair, name='sair') 
]  
   