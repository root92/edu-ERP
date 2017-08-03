# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0004_auto_20170727_1356'),
        ('student', '0003_auto_20170726_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('date', models.DateField()),
                ('present', models.BooleanField(default=True, verbose_name='Present?')),
                ('remark', models.CharField(max_length=200)),
                ('total_presence', models.IntegerField()),
                ('classLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.ClassLevel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Subject')),
            ],
        ),
    ]