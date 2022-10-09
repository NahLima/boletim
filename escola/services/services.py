import email
from escola.models import Aluno, Boletim, Disciplina, NotasBoletim
#from escola.views import aluno_detail, notas_boletim_list

def get_all_alunos():
    return Aluno.objects.all()


def get_aluno_infos(aluno_id=None, email=None, nome=None, data_nascimento=None):
    aluno = None

    if aluno_id is not None:
        aluno= Aluno.objects.get(id=aluno_id)
    elif email is not None:
       aluno = Aluno.objects.get(email=email)
    elif nome is not None:
        aluno = Aluno.objects.get(nome=nome)
    elif data_nascimento is not None:
        aluno =  Aluno.objects.get(data_nascimento=data_nascimento)
    return aluno


def get_disciplinas_infos(disciplina=None, carga_horaria=None):
    disciplina_info = None

    if disciplina is not None:
        disciplina_info= Disciplina.objects.get(disciplina=disciplina)

    elif carga_horaria is not None:
       disciplina_info = Disciplina.objects.get(carga_horaria=carga_horaria)

    return disciplina_info


def get_all_disciplinas():
    return Disciplina.objects.all()

def get_all_boletins():
    return Boletim.objects.all()


def get_boletins_infos(data_entrega=None, aluno_id=None):
    boletim_info = None

    if data_entrega is not None:
        boletim_info= Boletim.objects.get(data_entrega=data_entrega)

    elif aluno_id is not None:
       boletim_info = Boletim.objects.get(aluno=aluno_id)

    return boletim_info


def get_all_notas_boletins():
    return NotasBoletim.objects.all()


def get_notas_boletins_infos(disciplina=None, boletim=None, nota=None):
    nota_boletim_info = None

    if disciplina is not None:
        nota_boletim_info= NotasBoletim.objects.get(disciplina=disciplina)

    elif boletim is not None:
      nota_boletim_info = NotasBoletim.objects.get(boletim=boletim)

    elif nota is not None:
      nota_boletim_info = NotasBoletim.objects.filter(nota=nota)

    return nota_boletim_info

