from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from capacity.serializers import CapacitySerializer

class CapacityView(APIView):
    # def get(self, request):
    #     return Response(
    #         'please send query to endpoint URL:port/capacity followed' \
    #         'by ordered planeId and passenger numebrs respectively',
    #         status=400
    #     )


    def post(self, request):
        print(f'request.data: {request.data}\n')
        serializer = CapacitySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        # resp = serializer.save()
        serializer.save()
        # print(resp)
        # print(serializer.validated_data)
        return Response(serializer.data)

