from django.shortcuts import render

# Create your views here.

import django_filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from sample.models import SampleName
from sample.serializer import SampleSerializer

class SampleViewSet(viewsets.ModelViewSet):
    queryset = SampleName.objects.all()
    serializer_class = SampleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
