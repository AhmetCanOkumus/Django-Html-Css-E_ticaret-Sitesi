# Generated by Django 4.1.2 on 2022-10-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainproject', '0002_notebook_resim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='link',
            field=models.CharField(max_length=500),
        ),
    ]