# Generated by Django 4.0.3 on 2022-03-14 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
    ]