# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-12 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('username', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=32)),
                ('gender', models.IntegerField(default=1)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=50)),
                ('state', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'tlxy_users',
            },
        ),
    ]
