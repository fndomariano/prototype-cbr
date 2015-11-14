# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptcc', '0002_remove_regras_monitoramento'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoramento',
            name='solucao_sugerida',
            field=models.TextField(null=True),
        ),
    ]
