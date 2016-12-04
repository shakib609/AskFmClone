# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20160904_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answered_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='time',
            new_name='created',
        ),
    ]
