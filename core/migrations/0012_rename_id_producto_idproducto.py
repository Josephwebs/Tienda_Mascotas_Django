# Generated by Django 4.0.5 on 2022-06-14 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_producto_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='id',
            new_name='idproducto',
        ),
    ]