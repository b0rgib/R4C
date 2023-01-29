from rest_framework import serializers
from . models import Robot


class RobotSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=2, min_length=2)
    version = serializers.CharField(max_length=2, min_length=2)
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")