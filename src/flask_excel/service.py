from flask import Flask
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        dataframe = pd.read_csv("data.csv")
        return dataframe.to_json(orient="records")

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)