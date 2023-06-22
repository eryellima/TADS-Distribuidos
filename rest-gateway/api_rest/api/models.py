from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    buff = models.CharField(max_length=200)
    Item_Receita = models.ForeignKey(on_delete=models.CASCADE, related_name='item')

    def __str__(self):
        return self.nome
    
class Item_Receita(models.Model):
    item1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item1')
    item2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item2')

class Build(models.Model):
    item1 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item1')
    item2 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item2')
    item3 = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item3')

class Champion_Habilidade(models.Models):
    nome = models.CharField(max_length=200)
    ativo = models.BooleanField(default=False)
    descricao = models.TextField()
    dano = models.IntegerField()

    def __str__(self):
        return self.nome

class Origem(models.Model):
    nome = models.CharField(max_length=200)
    bonus = models.TextField()

    def __str__(self):
        return self.nome
    
class Classe(models.Model):
    nome = models.CharField(max_length=200)
    bonus = models.TextField()

    def __str__(self):
        return self.nome
    
class Champion(models.Model):
    nome = models.CharField(max_length=200)
    origem = models.ForeignKey(Origem, on_delete=models.CASCADE, related_name='origem')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='classe')
    build = models.ForeignKey(Build, on_delete=models.CASCADE, related_name='build')
    custo = models.IntegerField()
    vida = models.IntegerField()
    mana = models.IntegerField()
    armadura = models.IntegerField()
    ap = models.IntegerField()
    dps = models.IntegerField()
    dano = models.IntegerField()
    crti_rate = models.IntegerField()
    alcance = models.IntegerField()
    habilidade = models.ForeignKey(Champion_Habilidade, on_delete=models.CASCADE, related_name='habilidade')

    def __str__(self):
        return self.nome
    
class Melhoria(models.Model):
    TIERS = (
        ('Prata', 'Prata'),
        ('Ouro', 'Ouro'),
        ('Prismatico', 'Prismático')
    )

    nome = models.CharField(max_length=200)
    bonus = models.TextField()
    tier = models.CharField(max_length=20, choices=TIERS)

    def __str__(self):
        return self.nome
"""
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Livro(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    description = models.TextField()
    cover_image_url = models.ImageField(upload_to='livros/')

    def __str__(self):
        return self.title
"""