# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20160810_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='asked_by',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True, related_name='asked_by_question', default=None),
        ),
        migrations.AlterField(
            model_name='question',
            name='asked_to',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='asked_questions'),
        ),
    ]
