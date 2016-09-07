# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20160907_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
