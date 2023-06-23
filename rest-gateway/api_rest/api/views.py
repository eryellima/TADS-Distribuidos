from rest_framework import viewsets
from .models import Champion, Origem, Classe, Item_Basico, Item_Completo, Item_Receita, Build, Melhoria
from .serializers import ChampionSerializer, OrigemSerializer, ClasseSerializer, ItemBasicoSerializer, ItemReceitaSerializer, ItemCompletoSerializer, BuildSerializer, MelhoriaSerializer

#from .models import Task, Livro
#from .serializers import TaskSerializer, LivroSerializer


class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer

class OrigemViewSet(viewsets.ModelViewSet):
    queryset = Origem.objects.all()
    serializer_class = OrigemSerializer

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class ItemBasicoViewSet(viewsets.ModelViewSet):
    queryset = Item_Basico.objects.all()
    serializer_class = ItemBasicoSerializer

class ItemReceitaViewSet(viewsets.ModelViewSet):
    queryset = Item_Receita.objects.all()
    serializer_class = ItemReceitaSerializer

class ItemCompletoViewSet(viewsets.ModelViewSet):
    queryset = Item_Completo.objects.all()
    serializer_class = ItemCompletoSerializer

class BuildViewSet(viewsets.ModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer

class MelhoriaViewSet(viewsets.ModelViewSet):
    queryset = Melhoria.objects.all()
    serializer_class = MelhoriaSerializer


"""
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
"""