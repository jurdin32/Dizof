# Generated by Django 3.1.1 on 2020-09-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20200902_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='centro',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='slider',
            name='derecha',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='slider',
            name='izquierda',
            field=models.BooleanField(default=True),
        ),
    ]