from autos.models import *
from rest_framework import serializers


class AutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auto
        fields = ('nombre', 'descripcion')


class PerroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perro
        fields = ('nombre', 'descripcion')        