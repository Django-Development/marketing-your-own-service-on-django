# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBgColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
            ],
            options={
                'verbose_name': 'Item Background Color',
                'verbose_name_plural': 'Item Background Color',
            },
        ),
        migrations.CreateModel(
            name='AboutItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('short_description', models.TextField(blank=True, default=None, null=True)),
                ('image', models.ImageField(upload_to='about_items')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('color', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='About.AboutBgColor')),
            ],
            options={
                'verbose_name': 'About Item',
                'verbose_name_plural': 'About Items',
            },
        ),
        migrations.CreateModel(
            name='OurCustomers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('profession', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('short_description', models.TextField(blank=True, default=None, null=True)),
                ('image', models.ImageField(upload_to='customers_image')),
                ('facebook_profile', models.URLField(blank=True, default=None, null=True)),
                ('twitter_profile', models.URLField(blank=True, default=None, null=True)),
                ('linkedin_profile', models.URLField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Our Customers',
            },
        ),
    ]