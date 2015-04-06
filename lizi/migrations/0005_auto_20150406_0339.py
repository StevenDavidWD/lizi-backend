# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lizi', '0004_auto_20150403_0247'),
    ]

    operations = [
        migrations.CreateModel(
            name='SquareReply',
            fields=[
                ('squarereply_id', models.AutoField(serialize=False, primary_key=True)),
                ('squarereply_content', models.CharField(max_length=1000)),
                ('squarereply_time', models.DateTimeField()),
                ('square_id', models.ForeignKey(to='lizi.Square')),
                ('user_id', models.ForeignKey(to='lizi.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='square_reply',
            name='square_id',
        ),
        migrations.RemoveField(
            model_name='square_reply',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='square_reply',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='teacher_id',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student_id',
            field=models.ForeignKey(to='lizi.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='code',
            name='course_id',
            field=models.ForeignKey(to='lizi.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(to='lizi.Teacher'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='square',
            name='course_id',
            field=models.ForeignKey(to='lizi.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='square',
            name='user_id',
            field=models.ForeignKey(to='lizi.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentcal',
            name='course_id',
            field=models.ForeignKey(to='lizi.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentcal',
            name='user_id',
            field=models.ForeignKey(to='lizi.User'),
            preserve_default=True,
        ),
    ]
