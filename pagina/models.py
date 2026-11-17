from django.db import models

class filme(models.Model):
    titulo = models.CharField(max_length=100)
    nota = models.FloatField()
    genero = models.CharField(max_length=50)
    ano = models.IntegerField()
    linguagem = models.CharField(max_length=50)
    
    def __str__(self):
            return self.titulo
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class projeto(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    descricao = models.TextField()    
    categoria = models.ForeignKey(
         Categoria,
           on_delete=models.SET_NULL,
           null=True,
           blank=True,
           )
    def __str__(self):
        return self.nome