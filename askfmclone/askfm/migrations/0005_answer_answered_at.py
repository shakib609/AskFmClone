# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('askfm', '0004_question_anonymous'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answered_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 25, 7, 54, 23, 392731, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
