# Generated by Django 4.2.7 on 2023-11-26 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app17', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='tipo',
        ),
    ]
