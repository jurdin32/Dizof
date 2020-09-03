# Generated by Django 3.1.1 on 2020-09-02 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_principal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='Slider')),
                ('frase1', models.CharField(max_length=100)),
                ('posicion_frase1', models.IntegerField(default=50)),
                ('palabra2', models.CharField(max_length=100)),
                ('posicion_frase2', models.IntegerField(default=50)),
                ('texto_decorativo', models.CharField(max_length=100)),
                ('posicion_texto_decorativo', models.IntegerField(default=50)),
            ],
        ),
    ]