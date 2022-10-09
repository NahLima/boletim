INSERT INTO escola_aluno (nome, email, data_nascimento) VALUES ('Talita', 'jaguatirica@teste.com','25/08/199'), ('Leandro', 'leoabreu@teste.com.br', '20/08/1995'), ('Amora', 'amorinha@teste.com.br', '28/07/1995') ;
select * from escola_aluno;

INSERT INTO escola_boletim (data_entrega, aluno_id) VALUES ('09/10/2022', 14), ('09/10/2022', 15), ('09/10/2022', 16);
select * from escola_boletim;

INSERT INTO escola_disciplina (disciplina, carga_horaria) VALUES ('matematica', 60), ('portugues', 70), ('geografia', 45), ('fisica', 60);
select * from escola_disciplina;

INSERT INTO escola_notasboletim (disciplina_id, boletim_id, nota) VALUES (10,8,10), (11,8,5), (12,8,8), (13,8,7), (10,9,10), (11,9,5), (12,9,8), (13,9,7), (10,10,0), (11,10,7), (12,10,8), (13,10,7);
select * from escola_boletim