from rest_framework import serializers
from .models import CadastroAluno

class CadastroAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroAluno
        fields = ['nome','sexo','dt_nasc','tel','cpf']