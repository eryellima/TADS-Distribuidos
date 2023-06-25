from django.urls import path
from gateway import views

urlpatterns = [
    path('champions/', views.Champion_list),
    path('champions/<int:pk>/', views.Champion_detail),

    path('origens/', views.Origem_list),
    path('origens/<int:pk>/', views.Origem_detail),

    path('classes/', views.Classe_list),
    path('classes/<int:pk>/', views.Classe_detail),
    
    path('itensBasicos/', views.ItemBasico_list),
    path('itensBasicos/<int:pk>/', views.ItemBasico_detail),

    path('itensReceitas/', views.ItemReceita_list),
    path('itensReceitas/<int:pk>/', views.ItemBasico_detail),

    path('itensCompletos/', views.ItemCompleto_list),
    path('itensComplestos/<int:pk>/', views.ItemCompleto_detail),

    path('melhorias/', views.Melhoria_list),
    path('melhorias/<int:pk>/', views.Melhoria_detail),
    # Adicione outras rotas conforme necessário para os outros modelos
]
