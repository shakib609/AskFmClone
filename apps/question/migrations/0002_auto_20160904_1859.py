# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('liked_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(to='question.Question')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('question', 'liked_by')]),
        ),
    ]
