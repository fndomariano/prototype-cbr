# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptcc', '0002_substancia_grupo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='substancia',
            name='grupo',
        ),
    ]
