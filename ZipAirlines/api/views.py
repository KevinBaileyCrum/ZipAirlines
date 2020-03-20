from rest_framework.response import Response
from rest_framework.views import APIView
import logging

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
        print(planeId)
        print(passengerNum)
        return 1

    def get(self, request):
        logger.error('request')
        logger.error(request.query_params)
        if request.query_params:
            logger.error('i exist')
            for planeId, passengerNum in zip(request.query_params.getlist('planeId'), request.query_params.getlist('passengerNum')):
                try:
                    assert (isinstance(planeId and passengerNum, int))
                    self.findCapacity(planeId, passengerNum)
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




