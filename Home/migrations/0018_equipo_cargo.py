# Generated by Django 3.1.1 on 2020-09-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0017_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='cargo',
            field=models.CharField(default='Desarrollador', max_length=60),
        ),
    ]
