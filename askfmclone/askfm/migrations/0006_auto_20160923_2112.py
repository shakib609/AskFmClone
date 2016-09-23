# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('askfm', '0005_answer_answered_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('followed_by', models.ForeignKey(related_name='followed_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='asked_by',
        ),
        migrations.RemoveField(
            model_name='question',
            name='asked_to',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('user', 'followed_by')]),
        ),
    ]
