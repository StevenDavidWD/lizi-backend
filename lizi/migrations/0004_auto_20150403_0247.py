# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lizi', '0003_auto_20150402_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentCal',
            fields=[
                ('cal_id', models.AutoField(serialize=False, primary_key=True)),
                ('course_id', models.ForeignKey(to='lizi.course')),
                ('user_id', models.ForeignKey(to='lizi.user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_head_img',
            field=models.ImageField(null=True, upload_to=b'photos/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
