from rest_framework import serializers
from .mathLib import findCapacity

class CapacitySerializer(serializers.Serializer):
    planeId = serializers.ListField(
        child = serializers.IntegerField(min_value=0, max_value=10)
    )
    passengerNum = serializers.ListField(
        child = serializers.IntegerField(min_value=0)
    )
    litersPerMinute = serializers.FloatField(required=False)
    minutesOfFlight = serializers.FloatField(required=False)

