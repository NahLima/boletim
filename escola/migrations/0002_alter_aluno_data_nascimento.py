# Generated by Django 4.1.2 on 2022-10-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.CharField(db_index=True, max_length=12, null=True, verbose_name='data_nascimento'),
        ),
    ]
