# Generated by Django 2.0.5 on 2018-05-12 13:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessaoAluno',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('usuarioAluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.Aluno')),
            ],
            options={
                'db_table': 'sessaoAluno',
                'managed': True,
            },
        ),
    ]
