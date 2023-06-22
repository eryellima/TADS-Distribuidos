from rest_framework import viewsets
from .models import Champion, Champion_Habilidade, Origem, Classe, Item, Item_Receita, Build, Melhoria
from .serializers import ChampionSerilizer, ChampionHabilidadeSerilizer, OrigemSerilizer, ClasseSerilizer, ItemSerilizer, ItemReceitaSerilizer, BuildSerilizer, MelhoriaSerilizer

#from .models import Task, Livro
#from .serializers import TaskSerializer, LivroSerializer


class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerilizer

class ChampionHabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Champion_Habilidade.objects.all()
    serializer_class = ChampionHabilidadeSerilizer

class OrigemViewSet(viewsets.ModelViewSet):
    queryset = Origem.objects.all()
    serializer_class = OrigemSerilizer

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerilizer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerilizer

class ItemReceitaViewSet(viewsets.ModelViewSet):
    queryset = Item_Receita.objects.all()
    serializer_class = ItemReceitaSerilizer

class BuildViewSet(viewsets.ModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerilizer

class MelhoriaViewSet(viewsets.ModelViewSet):
    queryset = Melhoria.objects.all()
    serializer_class = MelhoriaSerilizer


"""
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
"""