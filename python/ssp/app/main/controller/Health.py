from app.main import api
from flask_restful import Resource


class Health(Resource):

    def get(self):
        return {"status": "OK"}, 200


api.add_resource(Health, '/health/status')
