# Generated by Django 4.0.5 on 2022-06-29 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Todolist',
        ),
    ]
