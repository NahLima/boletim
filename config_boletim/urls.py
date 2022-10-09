from django.contrib import admin
from django.urls import re_path
from escola import views 


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^api/alunos/$', views.alunos_list),
    re_path(r'^api/alunos/id/(?P<aluno_id>[0-9]+)$', views.aluno_detail),
    re_path(r'^api/alunos/nome/(?P<nome>[a-z-A-Z]+)$', views.aluno_detail),
    re_path(r'^api/alunos/email/(?P<email>[/\w\w\w\w\w@\w\w\.com/]+)$', views.aluno_detail),
    re_path(r'^api/alunos/data_nascimento/(?P<data_nascimento>[/\d{2}\/\d{2}\/\d{4}/g]+)$', views.aluno_detail),
    re_path(r'^api/disciplinas/$', views.disciplinas_list),
    re_path(r'^api/disciplina/nome/(?P<disciplina>[a-z-A-Z]+)$', views.disciplina_detail),
    re_path(r'^api/disciplina/carga_horaria/(?P<carga_horaria>[0-9]+)$', views.disciplina_detail),
    re_path(r'^api/boletim/$', views.boletim_list),
    re_path(r'^api/boletim/create/$', views.boletim_list),
    re_path(r'^api/boletim/data_entrega/(?P<data_entrega>[/\d{2}\/\d{2}\/\d{4}/g]+)$', views.boletim_detail),
    re_path(r'^api/boletim/aluno/(?P<aluno_id>[0-9]+)$', views.boletim_detail),
    re_path(r'^api/notasboletim/$', views.notas_boletim_list),
    re_path(r'^api/notasboletim/notas/(?P<nota>[a-z-A-Z-0-9]+)$', views.nota_boletim_detail),
]
