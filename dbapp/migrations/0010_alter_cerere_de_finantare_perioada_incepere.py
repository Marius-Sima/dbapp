# Generated by Django 4.2.7 on 2023-11-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0009_cerere_de_finantare_perioada_incepere_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cerere_de_finantare',
            name='perioada_incepere',
            field=models.DateField(),
        ),
    ]