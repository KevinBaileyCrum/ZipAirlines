from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


class CapacityView(APIView):
    def get(self, request):
        data = request.data
        return Response(data)
