from django.contrib import admin
from escola.models import Aluno, Boletim, Disciplina, NotasBoletim


@admin.register(Aluno)
class Alunos(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['id', 'nome', 'email', 'data_nascimento']
    list_display = ['id', 'nome', 'email']

@admin.register(Disciplina)
class Disciplinas(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['id', 'disciplina', 'carga_horaria']
    list_display = ['id', 'disciplina']


@admin.register(Boletim)
class Boletins(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['id', 'aluno', 'data_entrega']
    list_display = ['id', 'aluno']

@admin.register(NotasBoletim)
class NotasBoletins(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['id', 'disciplina', 'boletim', 'nota']
    list_display= ['id', 'disciplina', 'boletim']
    