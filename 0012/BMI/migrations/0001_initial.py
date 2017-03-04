# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-06 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('gender', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=1, verbose_name='性别')),
                ('height', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='身高')),
                ('weight', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='体重')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='填写日期')),
            ],
            options={
                'verbose_name': 'BMI指数',
                'verbose_name_plural': '参数管理',
            },
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('ip', models.GenericIPAddressField(primary_key=True, serialize=False, verbose_name='IP')),
                ('blackone', models.BooleanField(default=False, verbose_name='黑名单')),
                ('latestvisit', models.DateTimeField(auto_now_add=True, verbose_name='最近访问')),
                ('remark', models.TextField(blank=True, max_length=100, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': 'IP管理',
            },
        ),
        migrations.AddField(
            model_name='info',
            name='ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BMI.Ip', verbose_name='IP'),
        ),
    ]
