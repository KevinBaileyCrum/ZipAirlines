from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from math import log

# Get an instance of a logger
logger = logging.getLogger(__name__)

class IndexView(APIView):
    def get(self, request):
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
        return fuelCapacity / litersPerMinute

    def get(self, request):
        logger.error('request')
        logger.error(request.query_params)
        if request.query_params:
            try:
                assert (len(request.query_params.getlist('planeId')) == len(request.query_params.getlist('passengerNum'))), 'MISSING PARAMETER ERROR: include a planeId and passengerNum for each plane'
                for planeId, passengerNum in zip(request.query_params.getlist('planeId'), request.query_params.getlist('passengerNum')):
                        assert (planeId.isnumeric() and passengerNum.isnumeric()), 'PARAMETER ERROR: please ensure both planeId and passengerNum are type int'
                        minutesOfFlight = self.findCapacity(float(planeId), float(passengerNum))
                        return Response(
                            minutesOfFlight,
                            status=200
                        )
            except AssertionError as error:
                errorMsg = "ERROR-- "+str(error)
                return Response(
                    errorMsg,
                    status=401
                )

        else:
            return Response(
                'please enter up to ten ordered int:->planeId, int:->num_passanger respectively'
                'please send query to endpoint URL:port/capacity followed' \
                'by ordered planeId and passanger numebrs respectively',
                status=400
            )




