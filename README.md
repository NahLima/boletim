# boletim


- Ao baixar o git é necessário rodar instalar as dependecias elas estão descritas no arquivo requirements.txt

- Conectar o sqlite pegar o arquivo db.sqlite3 
- Na pasta sqlite_query tem um arquivo com as queries
- Rodar as queries

- rodar o python manage.py runserver para subir a aplicação



OBS:
  Usei o postman para testar as alterações e para criar novas informações. 

  O que falta ser feito:
  - melhorias de código
  - testes unitários
  - uma api que consolide as informações do aluno com suas notas etc
  - melhorar nomenclaturas 



```

Exemplos de uso:


http://127.0.0.1:8000/api/alunos/

    {
        "id": 14,
        "created_at": null,
        "update_at": null,
        "deleted_at": null,
        "nome": "Talita",
        "email": "jaguatirica@teste.com",
        "data_nascimento": "25/08/199"
    },

http://127.0.0.1:8000/api/alunos/nome/Talita

{
    "id": 14,
    "created_at": null,
    "update_at": null,
    "deleted_at": null,
    "nome": "Talita",
    "email": "jaguatirica@teste.com",
    "data_nascimento": "25/08/199"
}

http://127.0.0.1:8000/api/disciplina/nome/fisica

{
    "id": 13,
    "created_at": null,
    "update_at": null,
    "deleted_at": null,
    "disciplina": "fisica",
    "carga_horaria": 60
}

http://127.0.0.1:8000/api/disciplina/nome/matematica
PUT:
POSTMAN --> BODY --> ROW:

{
        "disciplina": "matematica",
        "carga_horaria": 65
}






