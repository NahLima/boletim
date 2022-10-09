import json
import re
from unittest import result
from django.shortcuts import render
from escola.models import Aluno, Disciplina, Boletim, NotasBoletim
from escola.services.services import get_all_alunos, get_aluno_infos,  \
    get_all_disciplinas,get_disciplinas_infos, get_all_boletins, get_boletins_infos, \
    get_all_notas_boletins, get_notas_boletins_infos
from escola.serializer import AlunoSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from escola.serializer import AlunoSerializer, DisciplinaSerializer, \
                            BoletimSerializer, NotasBoletimSerializer
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
def alunos_list(request):
    if request.method == 'GET':
        alunos = get_all_alunos()
        
        nome = request.query_params.get('nome', None)
        if nome is not None:
            alunos = alunos.filter(nome__icontains=nome)
        
        alunos_serializer = AlunoSerializer(alunos, many=True)
        return JsonResponse(alunos_serializer.data, safe=False)

 
    elif request.method == 'POST':
        aluno_data = JSONParser().parse(request)
        aluno_serializer = AlunoSerializer(data=aluno_data)
        if aluno_serializer.is_valid():
            aluno_serializer.save()
            return JsonResponse(aluno_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(aluno_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET', 'PUT', 'DELETE'])
def aluno_detail(request, aluno_id=None, nome=None, email=None, data_nascimento=None):
    try: 
        aluno = get_aluno_infos(aluno_id=aluno_id, nome=nome, email=email, data_nascimento=data_nascimento)
    except Aluno.DoesNotExist: 
        return JsonResponse({'message': 'O aluno não existe'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        aluno_serializer = AlunoSerializer(aluno) 
        return JsonResponse(aluno_serializer.data) 
    
    elif request.method == 'PUT': 
        aluno_data = JSONParser().parse(request) 
        aluno_serializer = AlunoSerializer(aluno, data=aluno_data) 
        if aluno_serializer.is_valid(): 
           aluno_serializer.save() 
           return JsonResponse(aluno_serializer.data) 
        return JsonResponse(aluno_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        aluno.delete() 
        return JsonResponse({'message': 'aluno foi deletado!'}, status=status.HTTP_204_NO_CONTENT)

      
@api_view(['GET', 'POST'])
def disciplinas_list(request):
    if request.method == 'GET':
        disciplina = get_all_disciplinas()
        disciplina_serializer = DisciplinaSerializer(disciplina, many=True)
        return JsonResponse(disciplina_serializer.data, safe=False)

    elif request.method == 'POST':
        disciplina_data = JSONParser().parse(request)
        disciplina_serializer = DisciplinaSerializer(data=disciplina_data)
        if disciplina_serializer.is_valid():
            disciplina_serializer.save()
            return JsonResponse(disciplina_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(disciplina_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def disciplina_detail(request, disciplina=None, carga_horaria=None):
    try: 
        disciplina = get_disciplinas_infos(disciplina=disciplina, carga_horaria=carga_horaria)
    except Disciplina.DoesNotExist: 
        return JsonResponse({'message': 'não existe'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        disciplina_serializer = DisciplinaSerializer(disciplina) 
        return JsonResponse(disciplina_serializer.data) 
    
    elif request.method == 'PUT': 
        disciplina_data = JSONParser().parse(request) 
        disciplina_serializer = DisciplinaSerializer(disciplina, data=disciplina_data) 
        if disciplina_serializer.is_valid(): 
           disciplina_serializer.save() 
           return JsonResponse(disciplina_serializer.data) 
        return JsonResponse(disciplina_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        disciplina.delete() 
        return JsonResponse({'message': 'disciplina foi deletada!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def boletim_list(request):
    if request.method == 'GET':
        boletim = get_all_boletins()
        boletim_serializer = BoletimSerializer(boletim, many=True)
        return JsonResponse(boletim_serializer.data, safe=False)

    elif request.method == 'POST':
        boletim_data = JSONParser().parse(request)
        boletim_serializer = BoletimSerializer(data=boletim_data)
        if boletim_serializer.is_valid():
            boletim_serializer.save()
            return JsonResponse(boletim_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(boletim_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def boletim_detail(request, data_entrega=None, aluno_id=None):
    try: 
        boletim = get_boletins_infos(data_entrega=data_entrega, aluno_id=aluno_id)
    except Boletim.DoesNotExist: 
        return JsonResponse({'message': 'não existe'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        boletim_serializer = BoletimSerializer(boletim) 
        return JsonResponse(boletim_serializer.data) 
    
    elif request.method == 'PUT': 
        boletim_data = JSONParser().parse(request) 
        boletim_serializer = BoletimSerializer(boletim, data=boletim_data) 
        if boletim_serializer.is_valid(): 
           boletim_serializer.save() 
           return JsonResponse(boletim_serializer.data) 
        return JsonResponse(boletim_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        boletim.delete() 
        return JsonResponse({'message': 'boletim foi deletado!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def notas_boletim_list(request):
    if request.method == 'GET':
        notas_bol = get_all_notas_boletins()
        notas_bol_serializer = NotasBoletimSerializer(notas_bol, many=True)
        return JsonResponse(notas_bol_serializer.data, safe=False)

    elif request.method == 'POST':
        notas_bol_data = JSONParser().parse(request)
        notas_bol_serializer = NotasBoletimSerializer(data=notas_bol_data)
        if notas_bol_serializer.is_valid():
           notas_bol_serializer.save()
           return JsonResponse(notas_bol_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(notas_bol_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def nota_boletim_detail(request, disciplina=None, boletim=None, nota=None):
    try: 
        nota_boletim =  get_notas_boletins_infos(disciplina=None, boletim=None, nota=None)
    except NotasBoletim.DoesNotExist: 
        return JsonResponse({'message': 'não existe'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        nota_boletim_serializer = NotasBoletimSerializer(nota_boletim) 
        return JsonResponse(nota_boletim_serializer.data) 
    
    elif request.method == 'PUT': 
        nota_boletim_data = JSONParser().parse(request) 
        nota_boletim_serializer = NotasBoletimSerializer(boletim, data=nota_boletim_data) 
        if nota_boletim_serializer.is_valid(): 
           nota_boletim_serializer.save() 
           return JsonResponse(nota_boletim_serializer.data) 
        return JsonResponse(nota_boletim_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        nota_boletim.delete() 
        return JsonResponse({'message': 'apagado!'}, status=status.HTTP_204_NO_CONTENT)
