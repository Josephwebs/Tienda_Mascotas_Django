# Generated by Django 4.0.5 on 2022-07-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='static/images/fundaciones/5.png', upload_to='static/images/upload/'),
        ),
    ]