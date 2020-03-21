from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from math import log

# Get an instance of a logger
logger = logging.getLogger(__name__)

class IndexView(APIView):
    def get(self, request):
        logger.error('hello i am a logger')
        return Response(
            'please send query to endpoint URL:port/capacity followed' \
            'by ordered planeId and passanger numebrs respectively',
            status=400
        )




class CapacityView(APIView):

    def findCapacity(self, planeId: int, passengerNum: int) -> int:
        print(f'planeId: {planeId} passengerNum: {passengerNum}')
        fuelCapacity = 200 * planeId
        litersPerMinute = (log(planeId) * .80) + (.002 * passengerNum) # log base 2
        minutesOfFlight = fuelCapacity / litersPerMinute
        print(minutesOfFlight)
        return minutesOfFlight

    def get(self, request):
        logger.error('request')
        logger.error(request.query_params)
        if request.query_params:
            for planeId, passengerNum in zip(request.query_params.getlist('planeId'), request.query_params.getlist('passengerNum')):
                try:
                    assert (planeId.isnumeric and passengerNum.isnumeric)
                    minutesOfFlight = self.findCapacity(float(planeId), float(passengerNum))
                    return Response(
                        minutesOfFlight,
                        status=200
                    )
                except AssertionError as error:
                    errorMsg = 'PARAMETER ERROR: please ensure both planeId and passengerNum are type int {}'.format(error)
                    return Response(
                        errorMsg,
                        status=401
                    )

            return Response({'test': 'it worked'})
        else:
            return Response(
                'please enter up to ten ordered int:->planeId, int:->num_passanger respectively'
                'please send query to endpoint URL:port/capacity followed' \
                'by ordered planeId and passanger numebrs respectively',
                status=400
            )




