import requests

if __name__ == '__main__':
    req = requests.get('http://localhost:8000/capacity/?planeId=1&passengerNums=1')
    print(req)
    req.json()
    print(req.data)
