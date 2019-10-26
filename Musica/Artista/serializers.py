from rest_framework import serializers 
from .models import Artista

class ArtistaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ('id','Nombre_Real','Nombre_Artistico','Edad','Pais_Origen','Nacionalidad','Inicio_Actividad')

    def created(self,validated_data):
        return Artista.objects.create(**validated_data)
    
    def upgrade(self,instance,validated_data):
        instance.Nombre_Real = validated_data.get('Nombre_Real', instance.Nombre_Real)
        instance.Nombre_Artistico = validated_data.get('Nombre_Artistico', instance.Nombre_Artistico)
        instance.Edad = validated_data.get('Edad',instance.Edad)
        instance.Pais_Origen = validated_data('Pais_Origen',instance.Pais_Origen)
        instance.Nacionalidad = validated_data('Nacionalidad', instance.Nacionalidad)
        instance.Inicio_Actividad = validated_data('Inicio_Actividad',instance.Inicio_Actividad)
        instance.save()
        return instance
