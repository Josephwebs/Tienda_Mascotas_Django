from rest_framework import serializers
from core.models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['idMascota', 'nombreMascota', 'edadAnioMascota','edadMesesMascota','sexoMascota','estEstirizadoMascota','razaMascota','fotoMascota']
    