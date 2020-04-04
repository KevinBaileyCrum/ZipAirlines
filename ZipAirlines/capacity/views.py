from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from capacity.serializers import CapacitySerializer

class CapacityView(APIView):
    def get(self, request):
        return Response(
            'please send query to endpoint URL:port/capacity followed' \
            'by ordered planeId and passanger numebrs respectively',
            status=400
        )


    def post(self, request):
        print(request.query_params)
        serializer = CapacitySerializer(data=request.query_params, many=True)
        serializer.is_valid(raise_exception=True)
        resp = serializer.save()
        print(resp)
        print(serializer.validated_data)
        return Response('hello')

