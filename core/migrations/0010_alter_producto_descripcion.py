# Generated by Django 4.0.5 on 2022-06-14 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_producto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='...', max_length=500, verbose_name='Descripcion Producto'),
        ),
    ]
