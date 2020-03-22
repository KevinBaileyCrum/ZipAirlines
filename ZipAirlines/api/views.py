from rest_framework.response import Response
from rest_framework.views import APIView
from math import log
import json
# statment of assumptions:
#   allows user to input [1,10] planeId ranging from 1 to 10
#   log is assumed to be natural log (base e)
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
            fuelCapacity = 200 * planeId
            litersPerMinute = (log(planeId) * .80) + (.002 * passengerNum) # natural log
            minutesOfFlight = fuelCapacity / litersPerMinute
            return (litersPerMinute, minutesOfFlight)

    def get(self, request):
        if request.query_params:
            try:
                responseList = list()
                planeIds = request.query_params.getlist('planeId')
                passengerNums = request.query_params.getlist('passengerNum')
                assert (len(planeIds) == len(passengerNums)), 'MISSING PARAMETER ERROR: include a planeId and passengerNum for each plane'
                assert (len(planeIds) > 0 and len(planeIds) < 11), 'planeId ERROR: please ensure queried planeId(s) is/are between 1 and 10'
                for planeId, passengerNum in zip(planeIds, passengerNums):
                        assert (planeId.isnumeric() and passengerNum.isnumeric()), 'PARAMETER ERROR: please ensure both planeId and passengerNum are type int'
                        assert (float(planeId) > 0 and float(planeId) < 11), 'planeId ERROR: planeIds must be between 1 and 10'
                        litersPerMinute, minutesOfFlight  = self.findCapacity(float(planeId), float(passengerNum))
                        jsonObj = {"planeId": planeId, "passengerNum": passengerNum, "litersPerMinute": litersPerMinute, "minutesOfFlight": minutesOfFlight}
                        json.dumps(jsonObj)
                        responseList.append(jsonObj)
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
            except ZeroDivisionError:
                errorMsg = f'ERROR your queried params resulted in a division by zero planeId:{planeId} passengerNum:{passengerNum}'
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

