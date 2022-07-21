
from . import views
from django.urls import  path



urlpatterns = [
    path('',views.index,name='home'),
    path('jogo/<int:id>/',views.jogo,name='jogo_user'),
    path('categoria/<str:categoria>/',views.categoria,name='categoria'),
    path('plat/<str:plataforma>/',views.plataforma,name='plataforma'),
    path('ordenar/<str:ordenacao>/',views.ordenar,name='ordenar')
]