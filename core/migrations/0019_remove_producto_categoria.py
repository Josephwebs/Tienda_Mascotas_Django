# Generated by Django 4.0.5 on 2022-07-01 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
    ]