# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askfm', '0003_auto_20160823_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
