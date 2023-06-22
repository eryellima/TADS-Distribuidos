from django.contrib import admin
from .models import Champion, Champion_Habilidade, Origem, Classe, Item, Item_Receita, Build, Melhoria

#from .models import Task, Livro


# Register your models here.
admin.site.register(Champion)
admin.site.register(Champion_Habilidade)
admin.site.register(Origem)
admin.site.register(Classe)
admin.site.register(Item)
admin.site.register(Item_Receita)
admin.site.register(Build)
admin.site.register(Melhoria)


"""
admin.site.register(Task)
admin.site.register(Livro)
"""