# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptcc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='substancia',
            name='grupo',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
