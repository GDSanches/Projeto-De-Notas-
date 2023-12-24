from django.db import models


class DemoModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="demo_images")

    def __str__(self):
        return self.title
    

class Usuario(models.Model):

    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, blank=False, null=False, default='')
    idade = models.CharField(max_length=50,blank=False, null=False, default='')

    class Meta:
        verbose_name = ('usuario')
        ordering = ('usuario',)
        verbose_name_plural = ("usuarios")

    def __str__(self):
        return self.usuario
    
class Nota (models.Model):
        id = models.AutoField(primary_key=True)
        titulo = models.TextField(blank=False, null=False)
        conteudo = models.TextField(blank=False, null=False)
        usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

        def __str__(self):
            return self.id
        
