# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lizi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(unique=True, max_length=11),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_sex',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(unique=True, max_length=11),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_sex',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
