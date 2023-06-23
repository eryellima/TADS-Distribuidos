from rest_framework import serializers
from .models import Champion, Origem, Classe, Item_Basico, Item_Completo, Item_Receita, Build, Melhoria

#from .models import Task, Livro

class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = '__all__'

class OrigemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origem
        fields = '__all__'

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'

class ItemBasicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Basico
        fields = '__all__'

class ItemReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Receita
        fields = '__all__'

class ItemCompletoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Completo
        fields = '__all__'

class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = '__all__'

class MelhoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Melhoria
        fields = '__all__'


"""
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
"""