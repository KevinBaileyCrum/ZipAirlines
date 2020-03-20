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
    def runFunc(self):
        i = 9
        while i > 0:
            print(i)
            i -= 1

    def get(self, request):
        self.runFunc()
        return Response({'test': 'it worked'})



