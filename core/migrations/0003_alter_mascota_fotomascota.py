# Generated by Django 4.0.4 on 2022-06-01 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_sexo_tipomascota_raza_mascota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fotoMascota',
            field=models.ImageField(upload_to='static/images/upload/'),
        ),
    ]