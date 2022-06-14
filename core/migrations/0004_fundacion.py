# Generated by Django 4.0.2 on 2022-06-10 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_mascota_fotomascota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundacion',
            fields=[
                ('idFundacion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de Fundación')),
                ('nombreFundacion', models.CharField(max_length=150, verbose_name='Nombre de la Fundación')),
                ('descFundacion', models.CharField(max_length=250, verbose_name='Descripción de la Fundación')),
            ],
        ),
    ]