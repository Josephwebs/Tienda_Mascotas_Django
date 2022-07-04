from rest_framework import serializers
from core.models import Fundacion, Producto, Mascota


class ProductoSerializer(serializers.ModelSerializer):

    desc_categoria = serializers.CharField(source="categoria")

    class Meta:
        model = Producto
        fields = "__all__"


class MascotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mascota
        fields = ['idMascota', 'nombreMascota',
                  'edadAnioMascota', 'edadMesesMascota', 'sexoMascota', 'estEstirizadoMascota', 'razaMascota', 'fotoMascota']


class FundacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fundacion
        fields = "__all__"
