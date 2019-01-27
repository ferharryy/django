from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UsuarioSerializer, UsuarioMiniSerializer
from .models import Usuario
from rest_framework.response import Response


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def list(self, request, *args, **kwargs):
      usuarios = Usuario.objects.all()
      serializer = UsuarioMiniSerializer(usuarios, many=True)
      return Response(serializer.data)
