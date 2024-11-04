from django.urls import path
from . import views

urlpatterns = [
    path('', views.dologin, name='login'),
    path('dologin/', views.dologin, name='login'),
    path('painel/', views.painel, name='painel'),
    ##### ESTOQUE #####
    path('Cadastro_Estoque/', views.cadastro_estoque, name='cadastro_estoque'),
    path('upload_estoque/', views.upload_estoque, name='upload_estoque'),
    path('Cadastro_Grupos_Lote/', views.cadastro_estoque_grupos, name='cadastro_estoque'),
    path('upload_estoque_grupos/', views.upload_estoque_grupos, name='upload_estoque_grupos'),
    path('estgrupos/', views.estoque_grupos_pecas, name='estoque_grupos_pecas'),


    ]