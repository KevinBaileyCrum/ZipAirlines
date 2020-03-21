from rest_framework.response import Response
from rest_framework.views import APIView
import logging
from math import log

# Get an instance of a logger
logger = logging.getLogger(__name__)

# statment of assumptions:
#   allows user to input [1,10] planeId ranging from 1 to 10
#   log is assumed to be base 2
#   api allows for repeat of the same planeId to be queried
#   assertions are made to capture to a certain degree of usefulness to describe what could have raised exception
#       non-captured assertions of other malformed request queries are dictated to 404
#   overflow is not checked for passengers since the value of float is beyond a normal plane's capacity

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
                responseList = list()
                assert (len(request.query_params.getlist('planeId')) == len(request.query_params.getlist('passengerNum'))), 'MISSING PARAMETER ERROR: include a planeId and passengerNum for each plane'
                assert (len(request.query_params.getlist('planeId')) > 0 and len(request.query_params.getlist('planeId')) < 11), 'planeId ERROR: please ensure queried planeId(s) is/are between 1 and 10'
                for planeId, passengerNum in zip(request.query_params.getlist('planeId'), request.query_params.getlist('passengerNum')):
                        assert (planeId.isnumeric() and passengerNum.isnumeric()), 'PARAMETER ERROR: please ensure both planeId and passengerNum are type int'
                        assert (float(planeId) > 0 and float(planeId) < 11), 'planeId ERROR: planeIds must be between 1 and 10'
                        minutesOfFlight = self.findCapacity(float(planeId), float(passengerNum))
                        responseList.append(('planeId '+planeId, minutesOfFlight))
                return Response(
                    responseList,
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




