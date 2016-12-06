# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('askfm', '0006_auto_20160923_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(related_name='following', to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('following', 'followed_by')]),
        ),
        migrations.RemoveField(
            model_name='follow',
            name='user',
        ),
    ]
