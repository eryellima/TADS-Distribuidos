from django.urls import path
from gateway import views

urlpatterns = [
    path('api/champions/', views.Champion_list),
    path('api/champions/<int:pk>/', views.Champion_detail),

    path('api/origens/', views.Origem_list),
    path('api/origens/<int:pk>/', views.Origem_detail),

    path('api/classes/', views.Classe_list),
    path('api/classes/<int:pk>/', views.Classe_detail),
    
    path('api/itensBasicos/', views.ItemBasico_list),
    path('api/itensBasicos/<int:pk>/', views.ItemBasico_detail),

    path('api/itensReceitas/', views.ItemReceita_list),
    path('api/itensReceitas/<int:pk>/', views.ItemBasico_detail),

    path('api/itensCompletos/', views.ItemCompleto_list),
    path('api/itensComplestos/<int:pk>/', views.ItemCompleto_detail),

    path('api/melhorias/', views.Melhoria_list),
    path('api/melhorias/<int:pk>/', views.Melhoria_detail),
    # Adicione outras rotas conforme necessário para os outros modelos
]
