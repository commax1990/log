# Generated by Django 4.1 on 2022-09-17 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('mcnumber', models.CharField(max_length=10, verbose_name='MC number')),
            ],
            options={
                'verbose_name': 'Company',
            },
        ),
        migrations.CreateModel(
            name='dispatcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
            ],
            options={
                'verbose_name': 'Dispatcher',
            },
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
            ],
            options={
                'verbose_name': 'Driver',
            },
        ),
        migrations.CreateModel(
            name='trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.CharField(max_length=150, verbose_name='Unit Number')),
                ('plate_number', models.CharField(max_length=10, verbose_name='Plate Number')),
            ],
            options={
                'verbose_name': 'Trailer',
            },
        ),
        migrations.CreateModel(
            name='truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.CharField(max_length=150, verbose_name='Unit Number')),
                ('plate_number', models.CharField(max_length=10, verbose_name='Plate Number')),
            ],
            options={
                'verbose_name': 'Truck',
            },
        ),
        migrations.CreateModel(
            name='load',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itsnumber', models.IntegerField(verbose_name='ITS number')),
                ('load', models.IntegerField(verbose_name='#')),
                ('status', models.CharField(
                    choices=[('open', 'open'), ('delivered', 'delivered'), ('INVOICED', 'INVOICED'), ('Paid', 'Paid')],
                    default='open', max_length=9)),
                ('Company',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.company',
                                   verbose_name='Company')),
                ('dispatcher',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.dispatcher',
                                   verbose_name='Dispatcher')),
                ('driver',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.driver',
                                   verbose_name='Driver')),
                ('trailer',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.trailer',
                                   verbose_name='Trailer')),
                ('truck',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.truck',
                                   verbose_name='Truck')),
            ],
            options={
                'verbose_name': 'List load',
                'verbose_name_plural': 'List load',
            },
        ),
    ]