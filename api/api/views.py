from rest_framework.response import Response
from rest_framework.views import APIView

class IndexView(APIView):
    def get(self, request):
        return Response('please send query to endpoint URL:port/capacity followed by ordered planeId and passanger numebrs respectively')


class CapacityView(APIView):
    def get(self, request):
        return Response({'test': 'it worked'})


