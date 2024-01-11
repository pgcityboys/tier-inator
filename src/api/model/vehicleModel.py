class VehicleModel:
    def __init__(self, id: int, batteryLevel: int, currentRangeMeters: int, coordinates: dict[float, float]):
        self.id = id
        self.batteryLevel = batteryLevel
        self.currentRangeMeters = currentRangeMeters
        self.coordinates = coordinates

    def serialize(self):
        return {
            "id": self.id,
            "batteryLevel": self.batteryLevel,
            "currentRangeMeters": self.currentRangeMeters,
            "coordinates": self.coordinates,
        }
