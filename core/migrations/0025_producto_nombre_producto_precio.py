# Generated by Django 4.0.5 on 2022-07-04 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_fundacion_website_alter_fundacion_descfundacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.CharField(default='Producto para mascotas', max_length=50, verbose_name='Nombre Producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.PositiveIntegerField(default=10000),
        ),
    ]