# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20160810_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='asked_by',
            field=models.ForeignKey(related_name='asked_by_questions', to=settings.AUTH_USER_MODEL, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='asked_to',
            field=models.ForeignKey(related_name='asked_to_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
