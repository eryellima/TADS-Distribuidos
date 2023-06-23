from django.contrib import admin
from .models import Champion, Origem, Classe, Item_Basico,Item_Completo, Item_Receita, Build, Melhoria

#from .models import Task, Livro


# Register your models here.
admin.site.register(Champion)
admin.site.register(Origem)
admin.site.register(Classe)
admin.site.register(Item_Basico)
admin.site.register(Item_Completo)
admin.site.register(Item_Receita)
admin.site.register(Build)
admin.site.register(Melhoria)


"""
admin.site.register(Task)
admin.site.register(Livro)
"""