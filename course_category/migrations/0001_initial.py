# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-18 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCoursecategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name=b'Main Category Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Main Course Category',
                'verbose_name_plural': 'Main Course Categories',
            },
        ),
        migrations.CreateModel(
            name='MainCoursecategoryAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=100, null=True, verbose_name=b'Main Category Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_category.MainCoursecategory')),
            ],
        ),
        migrations.CreateModel(
            name='SubCoursecategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name=b'Sub Category Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Sub Course Category',
                'verbose_name_plural': 'Sub Course Categories',
            },
        ),
        migrations.CreateModel(
            name='SubCoursecategoryAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=100, null=True, verbose_name=b'Sub Category Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_category.SubCoursecategory')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='subcoursecategoryassign',
            unique_together=set([('course_id', 'category')]),
        ),
        migrations.AlterUniqueTogether(
            name='maincoursecategoryassign',
            unique_together=set([('course_id', 'category')]),
        ),
    ]