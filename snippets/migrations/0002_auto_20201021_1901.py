# Generated by Django 3.1.2 on 2020-10-21 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='sytle',
            new_name='style',
        ),
    ]
