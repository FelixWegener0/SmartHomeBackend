from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
import database_main as db
import handleDatabaseInteractions as dataBaseFunction
import Pythonlog as log

database = db.connectToDatabse()
cursor = db.connectCursor(database)

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)


class getAllDataBaseData(Resource):
    def get(self):
        result = dataBaseFunction.getAllData()
        return jsonify(result)


class helloWorld(Resource):
    def get(self):
        return jsonify('Hello world')


api.add_resource(getAllDataBaseData, '/allData')
api.add_resource(helloWorld, '/')


def runServer():
    log.info('Start flask API server as demon')
    app.run(host='0.0.0.0')
    db.databseColseConnect(database)
