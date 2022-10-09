from rest_framework import serializers
from escola.models import Aluno, Disciplina, Boletim, NotasBoletim


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class BoletimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boletim
        fields = '__all__'

class NotasBoletimSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotasBoletim
        fields = '__all__'
