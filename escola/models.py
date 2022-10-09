from django.db import models
from escola.mixins import TrackingEntity

class Aluno(TrackingEntity):

    nome = models.CharField('Nome', max_length=150, blank=False, null=True, db_index=True)
    email = models.CharField('email', max_length=150, blank=False, null=True, db_index=True)
    data_nascimento = models.CharField('data_nascimento', max_length=12, blank=False, null=True, db_index=True)

    def to_dict(self):
        aluno_info = {
            'nome': self.nome,
            'email': self.email,
            'data_nascimento': self.data_nascimento
        }
        return aluno_info

    def __str__(self) -> str:
        return f'{self.nome} info'


class Disciplina(TrackingEntity):
    disciplina = models.CharField('Disciplina', max_length=150, blank=False, null=False, db_index=True)
    carga_horaria = models.IntegerField()

    def to_dict(self):
        materias = {
            'disciplina': self.disciplina,
            'carga_horaria':self.carga_horaria
        }
        return materias


class Boletim(TrackingEntity):
    data_entrega = models.CharField('data_entrega', max_length=12, blank=False, null=False, db_index=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def to_dict(self):
        boletim = {
            'data_entrega':self.data_entrega,
            'aluno': self.aluno
        }
        return boletim


class NotasBoletim(TrackingEntity):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    boletim = models.ForeignKey(Boletim, on_delete=models.CASCADE)
    nota = models.CharField('Nota', max_length=5, blank=False, null=False, db_index=True)

    def to_dict(self):
        notas_boletim = {
            'disciplina': self.disciplina,
            'boletim': self.boletim,
            'nota': self.nota
        }
        return notas_boletim

