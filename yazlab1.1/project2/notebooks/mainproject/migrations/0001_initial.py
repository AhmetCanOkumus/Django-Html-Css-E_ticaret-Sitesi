# Generated by Django 4.1.2 on 2022-10-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=100)),
                ('modelismi', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('fiyat', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('isletimsistemi', models.CharField(max_length=100)),
                ('islemcimodeli', models.CharField(max_length=100)),
                ('diskkapasitesi', models.CharField(max_length=100)),
                ('bellekkapasitesi', models.CharField(max_length=100)),
                ('ekrankartimodeli', models.CharField(max_length=100)),
                ('siteismi', models.CharField(max_length=100)),
            ],
        ),
    ]