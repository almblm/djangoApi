from django.shortcuts import render

# Create your views here.

import django_filters
from rest_framework import viewsets,filters

from sample.models import SampleName
from sample.serializer import SampleSerializer

class SampleViewSet(viewsets.ModelViewSet):
    queryset = SampleName.objects.all()
    serializer_class = SampleSerializer
