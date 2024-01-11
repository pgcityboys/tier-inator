from http import HTTPStatus
from flask import Blueprint, request
from logger import get_logger
from api.model.vehicleModel import VehicleModel
from api.model.vehiclesModel import VehiclesModel
from api.schema.vehiclesSchema import VehiclesSchema
import requests
import os

logger = get_logger(__name__)

TIER_URL = "https://platform.tier-services.io"
TIER_HEADERS = {
    'X-Api-Key': os.environ['TIER_KEY']
}

vehicles_info_api = Blueprint('VehiclesInfoApi', __name__)


@vehicles_info_api.route('/vehicles')
def find_stations_info():
    try:
        RADIUS = 500
        args = request.args
        lat = args.get("lat", default=54.37, type=float)
        lon = args.get("lon", default=18.62, type=float)
        
        vehiclesInRadiusRequest = f"lat={lat}&lng={lon}&radius={RADIUS}"
        response = requests.get(TIER_URL + "/v1/vehicle?" + vehiclesInRadiusRequest, headers=TIER_HEADERS)
        vehicles_data = []
        for vehicle in response.json()["data"]:
            if vehicle['attributes']['isRentable'] is True:
                vehicles_data.append(get_vehicle_data(vehicle).serialize())
        result = VehiclesModel(vehicles_data)
        return VehiclesSchema().dump(result), HTTPStatus.OK
    except Exception as e:
        logger.error("Vehicles error: " + str(e))
        return "", HTTPStatus.BAD_REQUEST


def get_vehicle_data(json_row: dict) -> VehicleModel:
    vehicle_coordinates = {"lat": json_row['attributes']["lat"], "lon": json_row['attributes']["lng"]}
   
    return VehicleModel(
        json_row["id"],
        json_row['attributes']["batteryLevel"],
        json_row['attributes']["currentRangeMeters"],
        vehicle_coordinates,
    )
