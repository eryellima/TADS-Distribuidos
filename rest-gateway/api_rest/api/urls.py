from django.urls import path
from .views import ChampionViewSet, OrigemViewSet, ClasseViewSet, ItemBasicoViewSet, ItemReceitaViewSet, ItemCompletoViewSet, MelhoriaViewSet

#from .views import TaskViewSet, LivroViewSet

urlpatterns = [
    path('api/champions/', ChampionViewSet.as_view({'get': 'list', 'post': 'create'}), name='champion-list'),
    path('api/champions/<int:pk>/', ChampionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='champion-detail'),

    path('api/origens/', OrigemViewSet.as_view({'get': 'list', 'post': 'create'}), name='origem-list'),
    path('api/origens/<int:pk>/', OrigemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='origem-detail'),

    path('api/classes/', ClasseViewSet.as_view({'get': 'list', 'post': 'create'}), name='classe-list'),
    path('api/classes/<int:pk>/', ClasseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='classe-detail'),

    path('api/itensBasicos/', ItemBasicoViewSet.as_view({'get': 'list', 'post': 'create'}), name='itemBasiso-list'),
    path('api/itensBasicos/<int:pk>/', ItemBasicoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='itemBasico-detail'),

    path('api/itensReceitas/', ItemReceitaViewSet.as_view({'get': 'list', 'post': 'create'}), name='itemReceita-list'),
    path('api/itensReceitas/<int:pk>/', ItemReceitaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='itemReceita-detail'),

    path('api/itensCompletos/', ItemCompletoViewSet.as_view({'get': 'list', 'post': 'create'}), name='itemCompleto-list'),
    path('api/itensCompletos/<int:pk>/', ItemCompletoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='itemCompleto-detail'),

    path('api/melhorias/', MelhoriaViewSet.as_view({'get': 'list', 'post': 'create'}), name='melhoria-list'),
    path('api/melhorias/<int:pk>/', MelhoriaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='melhoria-detail'),
]


"""
urlpatterns = [
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='tarefa-list'),
    path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='tarefa-detail'),

    path('livros/', LivroViewSet.as_view({'get': 'list', 'post': 'create'}), name='tarefa-list'),
    path('livros/<int:pk>/', LivroViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='livro-detail'),
]
"""