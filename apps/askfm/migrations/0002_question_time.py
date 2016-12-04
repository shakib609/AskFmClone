# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askfm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 8, 15, 18, 14, 24, 455606, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
