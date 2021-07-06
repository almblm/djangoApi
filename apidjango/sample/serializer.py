from django.db.models import fields
from rest_framework import serializers
from sample.models import SampleName

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleName
        fields = ('name','bookType')