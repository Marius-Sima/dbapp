# Generated by Django 4.2.6 on 2023-10-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0002_remove_cerere_de_finantare_perioada_incepere_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cerere_de_finantare',
            name='programe',
            field=models.CharField(choices=[(1, 'Cultura'), (2, 'Mass Media'), (3, 'Educatie'), (4, 'Spiritualitate si Traditie'), (5, 'Societate Civila')], max_length=2),
        ),
    ]
