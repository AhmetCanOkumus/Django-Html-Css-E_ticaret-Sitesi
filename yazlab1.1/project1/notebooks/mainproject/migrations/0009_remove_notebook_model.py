# Generated by Django 4.1.2 on 2022-10-27 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainproject', '0008_remove_notebook_link1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='model',
        ),
    ]
