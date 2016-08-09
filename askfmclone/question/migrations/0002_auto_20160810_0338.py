# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='asked_to',
            field=models.ForeignKey(related_name='asked_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
