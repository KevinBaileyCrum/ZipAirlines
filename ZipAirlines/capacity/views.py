from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #TODO translate http status from number to readible
from capacity.serializers import CapacitySerializer

class CapacityView(APIView):
    def post(self, request):
        print(request.query_params)
        serializer = CapacitySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        return Response('hello')

