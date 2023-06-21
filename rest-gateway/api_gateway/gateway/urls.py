from django.urls import path
from . import views

urlpatterns = [
    path('gateway/', views.gateway, name='gateway'),
    # Adicione outros URLs dos seus serviços aqui
]
