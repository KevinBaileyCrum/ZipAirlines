from rest_framework.response import Response
from rest_framework.views import APIView
import logging

class IndexView(APIView):
    def get(self, request):
        return Response('please send query to endpoint URL:port/capacity followed by ordered planeId and passanger numebrs respectively')


class CapacityViewIndex(APIView):
    def get(self, request):
        return Response(
            'please enter up to ten ordered int:->planeId, int:->num_passanger respectively'
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



