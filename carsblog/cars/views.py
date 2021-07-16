from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from rest_framework import permissions


class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

    def create(self, request):
        ser = CarSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response("Created")
        else:
            return Response(f"Errors {ser.errors}")

# Create your views here.
