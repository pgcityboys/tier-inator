# mevo-inator
Microservice to get MEVO points

### Getting started
Install dependencies
```
pip install -r requirements.txt
```

Run app in debug mode
```
flask run --debug
```

Port can be set with env variable. E.g. `FLASK_RUN_PORT=2137`. To do this in development mode you can use `.flaskenv` file.
More options can be found in https://flask.palletsprojects.com/en/3.0.x/cli/.

### Documentation
- Flask: https://flask.palletsprojects.com/en/3.0.x/quickstart/
- Schemas: https://flask-marshmallow.readthedocs.io/en/latest/

### API
`GET /api/vehicles`
#### Parameters:
- lat - latitude of searched area.
- lon - longitude of searched area.
#### Example:
```
http://127.0.0.1:5000/api/vehicles?lat=54.2718&lon=18.616
```
Result
```
{
  "data": [
    {
      "id": str,
      "batteryLevel": int,
      "currentRangeMeters": int,
      "coordinates": {
        "lat": float,
        "lon": float
      }
    }
  ]
}
```