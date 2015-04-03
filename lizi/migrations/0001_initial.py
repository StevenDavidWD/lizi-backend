# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('course_id', models.AutoField(serialize=False, primary_key=True)),
                ('attend_time', models.DateTimeField()),
                ('attend_status', models.CharField(max_length=10)),
                ('attend_code', models.BigIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='code',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('attend_code', models.BigIntegerField()),
                ('attend_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_id', models.AutoField(serialize=False, primary_key=True)),
                ('course_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='square',
            fields=[
                ('square_id', models.AutoField(serialize=False, primary_key=True)),
                ('square_content', models.CharField(max_length=2000)),
                ('square_time', models.DateTimeField()),
                ('course_id', models.ForeignKey(to='lizi.course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='square_reply',
            fields=[
                ('squarereply_id', models.AutoField(serialize=False, primary_key=True)),
                ('squarereply_content', models.CharField(max_length=1000)),
                ('squarereply_time', models.DateTimeField()),
                ('square_id', models.ForeignKey(to='lizi.square')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('teacher_id', models.AutoField(serialize=False, primary_key=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=32)),
                ('teacher_real_name', models.CharField(max_length=20)),
                ('teacher_points', models.IntegerField(default=0)),
                ('teacher_mail', models.CharField(max_length=50)),
                ('teacher_head_img', models.CharField(max_length=255)),
                ('teacher_sex', models.IntegerField()),
                ('teacher_device_token', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=32)),
                ('user_real_name', models.CharField(max_length=20)),
                ('user_points', models.IntegerField(default=0)),
                ('user_mail', models.CharField(max_length=50)),
                ('user_head_img', models.CharField(max_length=255)),
                ('user_sex', models.IntegerField()),
                ('user_device_token', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='square_reply',
            name='user_id',
            field=models.ForeignKey(to='lizi.user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='square',
            name='user_id',
            field=models.ForeignKey(to='lizi.user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(to='lizi.teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='code',
            name='course_id',
            field=models.ForeignKey(to='lizi.course'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_id',
            field=models.ForeignKey(to='lizi.user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendance',
            name='teacher_id',
            field=models.ForeignKey(to='lizi.teacher'),
            preserve_default=True,
        ),
    ]
