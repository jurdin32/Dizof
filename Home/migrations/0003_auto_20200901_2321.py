# Generated by Django 3.1.1 on 2020-09-01 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_autores_proyectos'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='imagen',
            field=models.FileField(upload_to='projects/'),
        ),
    ]
