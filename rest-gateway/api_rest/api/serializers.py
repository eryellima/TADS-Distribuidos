from rest_framework import serializers
from .models import Champion, Champion_Habilidade, Origem, Classe, Item, Item_Receita, Build, Melhoria

#from .models import Task, Livro

class ChampionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = '__all__'

class ChampionHabilidadeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Champion_Habilidade
        fields = '__all__'

class OrigemSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Origem
        fields = '__all__'

class ClasseSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'

class ItemSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemReceitaSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Item_Receita
        fields = '__all__'

class BuildSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = '__all__'

class MelhoriaSerilizer(serializers.ModelSerializer):
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