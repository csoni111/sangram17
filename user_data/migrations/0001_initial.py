# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0004_auto_20170108_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyRegistrationSupplement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(help_text='Please fill your real name', max_length=100, verbose_name='Real name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('remarks', models.TextField(blank=True, verbose_name='Remarks')),
                ('registration_profile', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='_user_data_myregistrationsupplement_supplement', to='registration.RegistrationProfile', verbose_name='registration profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
