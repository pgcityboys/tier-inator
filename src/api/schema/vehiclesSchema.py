from flask_marshmallow import Schema

class VehiclesSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["data"]