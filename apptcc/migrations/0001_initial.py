# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bacia_Hidrografica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.AutoField(verbose_name=b'id', serialize=False, auto_created=True, primary_key=True)),
                ('valor_coletado', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Entorno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('variavel_entorno', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Monitoramento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_monitoramento', models.DateField(verbose_name=b'Data do Monitoramento')),
                ('classificacao_iap', models.CharField(max_length=45, null=True)),
                ('classificacao_iva', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ponto_Monitoramento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Regras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classificacao_iap', models.CharField(max_length=45)),
                ('classificacao_iva', models.CharField(max_length=45)),
                ('risco', models.CharField(max_length=1)),
                ('solucao_sugerida', models.TextField()),
                ('entorno', models.ForeignKey(to='apptcc.Entorno', on_delete=models.CASCADE)),                
            ],
        ),
        migrations.CreateModel(
            name='Rio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('dimensao', models.FloatField()),
                ('bacia_hidrografica', models.ForeignKey(to='apptcc.Bacia_Hidrografica', on_delete=models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Substancia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ponto_monitoramento',
            name='rio',
            field=models.ForeignKey(to='apptcc.Rio', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='monitoramento',
            name='ponto_monitoramento',
            field=models.ForeignKey(to='apptcc.Ponto_Monitoramento', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='coleta',
            name='ponto_monitoramento',
            field=models.ForeignKey(to='apptcc.Ponto_Monitoramento', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='coleta',
            name='substancia',
            field=models.ForeignKey(to='apptcc.Substancia', on_delete=models.CASCADE),
        ),
    ]
