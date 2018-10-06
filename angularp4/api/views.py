from autos.models import *
from rest_framework import viewsets
from .serializers import *


class AutoViewSet(viewsets.ModelViewSet):

    queryset = Auto.objects.all()
    serializer_class = AutoSerializer

class PerroViewSet(viewsets.ModelViewSet):

    queryset = Perro.objects.all()
    serializer_class = PerroSerializer
