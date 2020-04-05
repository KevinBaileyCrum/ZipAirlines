from rest_framework import serializers
from math import log
from .mathLib import CapacityObject

class CapacitySerializer(serializers.Serializer):
    planeId = serializers.IntegerField(min_value=0, max_value=10)
    passengerNum = serializers.IntegerField(min_value=0)
    # litersPerMinute = serializers.FloatField(required=False)
    # minutesOfFlight = serializers.FloatField(required=False)

    def create(self, validated_data):
        litersPerMinute, minutesOfFlight = self.findCapacity(
            self.validated_data['planeId'],
            self.validated_data['passengerNum']
        )
        Thang = CapacityObject(
            self.validated_data['planeId'],
            self.validated_data['passengerNum'],
            litersPerMinute,
            minutesOfFlight
        )
        print('Thang')
        print(repr(Thang))
        return Thang


    def findCapacity(self, planeId: int, passengerNum: int) -> float:
        fuelCapacity = 200 * planeId
        litersPerMinute = (log(planeId) * .80) + (.002 * passengerNum) # natural log
        minutesOfFlight = fuelCapacity / litersPerMinute
        return (litersPerMinute, minutesOfFlight)



