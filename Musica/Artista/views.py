from django.shortcuts import render

from .models import Artista
from .serializers import ArtistaSerializers

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ArtistaList(APIView):
    def get(self,request):

        Artistas = Artista.objects.all()
        serializer = ArtistaSerializers(Artistas, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ArtistaSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            Artista_saved = serializer.save()
        return Response({"succes": "Se Registro al artista '{}'".format(Artista_saved.Nombre_Artistico)})

    def put(self,request,pk):
        saved_Artista = get_object_or_404(Artista.objects.all(), pk=pk)
        serializer = ArtistaSerializers(instance=saved_Artista, data=request.data, partial= True)
        if serializer.is_valid(raise_exception=True):
            Artista_saved = serializer.save()
        return Response({"succes":"Se Actualizo al artista '{}'".format(Artista_saved.Nombre_Artistico)})

    def delete(self,request,pk):
        Artista_delete = get_object_or_404(Artista.objects.all(), pk=pk)
        Artista_delete.delete()
        return Response({"message":"Artista con id '{}' eliminado".format(pk)},status= 204)