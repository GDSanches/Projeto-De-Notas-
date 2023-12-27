
from rest_framework import serializers
from .models import Usuario, Nota

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = ["id", "usuario", "senha"]

class NotaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Nota
    fields = ["id", "titulo", "conteudo","usuario_id"]
