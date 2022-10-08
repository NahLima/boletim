import json
import re
from unittest import result
from django.shortcuts import render
from escola.models import Aluno
from rest_framework.response import Response
from rest_framework.views import APIView
from escola.services.aluno_svc import list_alunos, registro_aluno, get_aluno



class AlunoView(APIView):
    def get(self, request, id=None, *args, **Kwargs):
        if id is not None:
            result = get_aluno(aluno_id=id)
        else:
            result = list_alunos()

        return Response(result)

    def post(self, request, *args, **Kwargs):
        data = request.data

        nome = data.get('nome')
        email = data.get('email')
        data_nascimento = data.get('data_nascimento')

        result = registro_aluno(nome=nome, email=email, data_nascimento= data_nascimento)
        return Response(data = result)

    def put(self, request, aluno_id,  *args, **Kwargs):
        aluno_id = Aluno.objects.get(id=aluno_id)
        #update = Aluno(request.POST)
    
        #if update.is_valid():
            #nome = update.cleaned_data['nome']
            #email = update.cleaned_data['email']
            #data_nascimento = update.cleaned_data['data_nascimento']
            #query = Aluno(nome=nome, email=email, data_nascimento=data_nascimento)
            #query.save()

        return request
