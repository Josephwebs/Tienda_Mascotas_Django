# Generated by Django 4.0.5 on 2022-06-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_persona_alter_categoria_idcategoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='Hermosa bandana para tu peludo, disponible en distintos colores y diseños', max_length=500, verbose_name='Descripcion Producto'),
        ),
    ]
