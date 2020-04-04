from rest_framework import serializers
from .mathLib import findCapacity

class CapacitySerializer(serializers.Serializer):
    planeId = serializers.IntegerField(min_value=0, max_value=10)
    passengerNum = serializers.IntegerField(min_value=0)
    litersPerMinute = serializers.FloatField(required=False)
    minutesOfFlight = serializers.FloatField(required=False)

    def create(self, validated_data):
        litersPerMinute, minutesOfFlight = findCapacity(self.planeId, self.passengerNum)
        print(litersPerMinute, minutesOfFlight)


