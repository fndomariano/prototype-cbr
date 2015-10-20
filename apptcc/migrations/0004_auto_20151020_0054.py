# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptcc', '0003_remove_substancia_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoramento',
            name='classificacao_iap',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='monitoramento',
            name='classificacao_iva',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
