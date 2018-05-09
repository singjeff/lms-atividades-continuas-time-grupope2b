# Generated by Django 2.0.5 on 2018-05-09 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='Nome', max_length=30)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('celular', models.CharField(max_length=14, unique=True)),
                ('idlogin', models.CharField(db_column='idLogin', max_length=30, unique=True)),
                ('senha', models.CharField(max_length=15)),
                ('dtexpiracao', models.DateField(db_column='DtExpiracao')),
                ('ra', models.IntegerField(db_column='RA')),
                ('foto', models.CharField(db_column='Foto', max_length=50)),
            ],
            options={
                'db_table': 'Aluno',
                'managed': True,
            },
        ),
    ]
