from django.urls import path
from .views import ChampionViewSet, OrigemViewSet, ClasseViewSet, ItemViewSet, MelhoriaViewSet

#from .views import TaskViewSet, LivroViewSet

urlpatterns = [
    path('champions/', ChampionViewSet.as_view({'get': 'list', 'post': 'create'}), name='champion-list'),
    path('champions/<int:pk>/', ChampionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='champion-detail'),

    path('origens/', OrigemViewSet.as_view({'get': 'list', 'post': 'create'}), name='origem-list'),
    path('origens/<int:pk>/', OrigemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='origem-detail'),

    path('classes/', ClasseViewSet.as_view({'get': 'list', 'post': 'create'}), name='classe-list'),
    path('classes/<int:pk>/', ClasseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='classe-detail'),

    path('itens/', ItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='item-list'),
    path('itens/<int:pk>/', ItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='item-detail'),

    path('melhorias/', MelhoriaViewSet.as_view({'get': 'list', 'post': 'create'}), name='melhoria-list'),
    path('melhorias/<int:pk>/', MelhoriaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='melhoria-detail'),
]


"""
urlpatterns = [
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='tarefa-list'),
    path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='tarefa-detail'),

    path('livros/', LivroViewSet.as_view({'get': 'list', 'post': 'create'}), name='tarefa-list'),
    path('livros/<int:pk>/', LivroViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='livro-detail'),
]
"""