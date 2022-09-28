from rest_framework import serializers
from .models import Models, SuperType

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['type']
        