# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-02 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('state', models.CharField(choices=[(b'1', b'In Progress'), (b'2', b'Failed'), (b'3', b'Achieved')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('state', models.CharField(choices=[(b'1', b'In Progress'), (b'2', b'Failed'), (b'3', b'Achieved')], max_length=1)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.Goal')),
            ],
        ),
    ]