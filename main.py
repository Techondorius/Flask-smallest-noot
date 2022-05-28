from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
# CORS(
#     app,
#     supports_credentials=True
# )
api = Api(app)

class Noot(Resource):
    def get(self):
        return {"message":"got noot"}


api.add_resource(Noot, "/noot")

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')