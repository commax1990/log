# Generated by Django 4.1 on 2022-09-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spisok_MC_Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcnumber', models.TextField(blank=50, verbose_name='MCNumber')),
            ],
            options={
                'verbose_name': 'mcnumber',
                'verbose_name_plural': 'mcnumber',
                'ordering': ['mcnumber'],
            },
        ),
    ]
