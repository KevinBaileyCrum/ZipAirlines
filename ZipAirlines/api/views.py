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
            for planeId, passengerNum in zip(request.query_params['planeId'], request.query_params['passengerNum']):
            # for planeId, passengerNum in zip(request.query_params.items()):
                # for planeId, passengerNum in request.query_params['planeId'], request.query_params['pas']:
                print(planeId)
                print(passengerNum)
                #     self.findCapacity(planeId, passengerNum)
                # for key in request.query_params:
                # print(key)
            return Response({'test': 'it worked'})
        else:
            return Response(
                'please enter up to ten ordered int:->planeId, int:->num_passanger respectively'
                'please send query to endpoint URL:port/capacity followed' \
                'by ordered planeId and passanger numebrs respectively',
                status=400
            )




