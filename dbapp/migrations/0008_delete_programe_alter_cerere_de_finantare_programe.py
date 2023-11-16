# Generated by Django 4.2.6 on 2023-11-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0007_alter_cerere_de_finantare_programe'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Programe',
        ),
        migrations.AlterField(
            model_name='cerere_de_finantare',
            name='programe',
            field=models.CharField(choices=[('cultura', 'Cultura'), ('mass_media', 'Mass-Media'), ('educatie', 'Educatie'), ('spiritualitate', 'Spiritualitate si Traditie'), ('societate', 'Societate Civila')], max_length=30),
        ),
    ]
