import email
from escola.models import Aluno

def list_alunos():
    query = Aluno.objects.all()
    return [aluno.to_dict() for aluno in query]


def registro_aluno(nome, email, data_nascimento):
    novoUsuario = Aluno(nome=nome, email=email, data_nascimento=data_nascimento)
    novoUsuario.save()

def get_aluno(aluno_id):
    aluno = Aluno.objects.get(id=id)
    return aluno


    


        