# Generated by Django 3.1.1 on 2020-09-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_auto_20200904_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='historia',
            name='escritor',
            field=models.CharField(default='admin', max_length=60),
        ),
        migrations.AddField(
            model_name='historia',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='historia',
            name='visitas',
            field=models.IntegerField(default=1),
        ),
    ]
