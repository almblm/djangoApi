from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets,generics
from django_filters.rest_framework import DjangoFilterBackend

from sample.models import SampleName
from sample.serializer import SampleSerializer

class SampleViewSet(viewsets.ModelViewSet):
    queryset = SampleName.objects.all()
    serializer_class = SampleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class SampleListApi(generics.ListAPIView):
        queryset = SampleName.objects.all()
        serializer_class = SampleSerializer

class SampleCreateApi(generics.CreateAPIView):
        queryset = SampleName.objects.all()
        serializer_class = SampleSerializer

class SampleUpdateApi(generics.UpdateAPIView):
        queryset = SampleName.objects.all()
        serializer_class = SampleSerializer

class SampleDestoryApi(generics.DestroyAPIView):
        queryset = SampleName.objects.all()
        serializer_class = SampleSerializer