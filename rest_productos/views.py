from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto, Mascota, Fundacion
from .serializers import ProductoSerializer, MascotaSerializer, FundacionSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
# Create your views here.
def lista_productos(request):
    """
    Lista todos los Productos
    """

    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, statuts=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, statuts=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_mascotas(request):
    """
    Lista todas los Mascotas
    """

    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MascotaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, statuts=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, statuts=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_fundaciones(request):
    """
    Lista todas los fundaciones
    """

    if request.method == 'GET':
        fundacion = Fundacion.objects.all()
        serializer = FundacionSerializer(fundacion, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FundacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, statuts=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, statuts=status.HTTP_400_BAD_REQUEST)
