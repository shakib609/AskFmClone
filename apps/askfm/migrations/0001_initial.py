# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.TextField(null=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(max_length=300, default=None)),
                ('asked_by', models.ForeignKey(related_name='asked_by_questions', to=settings.AUTH_USER_MODEL, default=None, null=True)),
                ('asked_to', models.ForeignKey(related_name='asked_to_questions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(to='askfm.Question'),
        ),
    ]
