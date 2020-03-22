# ZipAirlines
a Django Rest Framework for planes and the people that sit in them

------------


## Running Locally
##### clone repo
`$git clone https://github.com/kevinbaileycrum/zipairlines.git`
##### Installing Dependencies:
With python3 install the dependencies noted by requirements.txt by running 
`$ pip install -r requirements.txt --no-index --find-links file:///tmp/packages`
*note: usage of a virtual environment is recommended*
##### Change into Project Directory and run Server
`$cd ZipAirlines`   

 `$python3 manage.py runserver`
 *note: you may see an error:*
 `You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. Run 'python manage.py migrate' to apply them.`
*to surpress the error run*
`manage.py migrate`

##### runs on localhost:8000/


## API SPECS:
The api accepts two endpoints where  URL:PORT is defined by either how the project is ran via locally (localhost:8000) or on the deployed site ()

##### endpoints:
`URL:PORT/` loads index endpoint
`URL:PORT/capacity/` loads capacity endpoint

##### capacity endpoint
Capacity/ accepts params in the form of query string (https://en.wikipedia.org/wiki/Query_string).  The query string is of the form:
`URL:PORT/capacity/?planeId=[int]&passengerNum=[int]`
*notice the trailing slash after capacity*
The parameters accepted by the api is the ordered pairing of planeId and passengerNum where planeId must be a number between 1 and 10 inclusively.  **The api only accepts between 1 and 10 (inclusively) planeId, passengerNum pairs **


## Testing
From repo root directory run `python3 tests.py`
------------


##### usage assumptions
- log is assumed to be a natural log of base e as per python's default `math.log`
- api allows for repeat of the same planeId to be queried
- assertions are made to capture to a certain degree of usefulness to describe what could have raised exception
- non-captured assertions of other malformed request queries are dictated to 404
- overflow is not checked for passengers since the value of float is beyond a normal plane's capacity






