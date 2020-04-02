from math import log

def findCapacity(self, planeId: int, passengerNum: int) -> float:
    fuelCapacity = 200 * planeId
    litersPerMinute = (log(planeId) * .80) + (.002 * passengerNum) # natural log
    minutesOfFlight = fuelCapacity / litersPerMinute
    return (litersPerMinute, minutesOfFlight)

