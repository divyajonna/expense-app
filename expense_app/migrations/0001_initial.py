# Generated by Django 2.0.10 on 2019-02-04 04:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('currency', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('timestampOfExpense', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='expense_app.Client')),
            ],
        ),
    ]