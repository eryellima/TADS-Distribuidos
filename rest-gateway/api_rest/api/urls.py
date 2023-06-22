from django.urls import path
from .views import TaskViewSet, LivroViewSet

urlpatterns = [
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='tarefa-list'),
    path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='tarefa-detail'),

    path('livros/', LivroViewSet.as_view({'get': 'list', 'post': 'create'}), name='tarefa-list'),
    path('livros/<int:pk>/', LivroViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='livro-detail'),
]