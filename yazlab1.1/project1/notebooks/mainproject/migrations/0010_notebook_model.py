# Generated by Django 4.1.2 on 2022-10-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainproject', '0009_remove_notebook_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='model',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
