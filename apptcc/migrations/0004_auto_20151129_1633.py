# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptcc', '0003_monitoramento_solucao_sugerida'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Regras',
            new_name='Casos',
        ),
        migrations.AddField(
            model_name='monitoramento',
            name='risco',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
