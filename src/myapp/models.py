from django.db import models


class Usuario(models.Model):

    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=False, null=False)
    senha = models.CharField(max_length=50,blank=False, null=False)

    class Meta:
        verbose_name = ('usuario')
        ordering = ('usuario',)
        verbose_name_plural = ("usuarios")

    def __str__(self):
        return self.id
    
class Nota (models.Model):
        id = models.AutoField(primary_key=True)
        titulo = models.TextField(blank=False, null=False)
        conteudo = models.TextField(blank=False, null=False)

        def __str__(self):
            return self.id
        
