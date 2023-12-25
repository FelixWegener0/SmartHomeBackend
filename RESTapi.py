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


class getAllTodaysData(Resource):
    def get(self):
        result = dataBaseFunction.getAllTodaysData()
        return jsonify(result)


class getAllTodaysDataForRoom(Resource):
    def get(self, room, allData):
        result = dataBaseFunction.getAllTodaysDataForRoom(room, allData)
        return jsonify(result)


class getLastEntyByRoom(Resource):
    def get(self, room):
        result = dataBaseFunction.getLastEntry(room)
        return jsonify(result)


class helloWorld(Resource):
    def get(self):
        return jsonify('Hello world')


api.add_resource(getLastEntyByRoom, '/getLastEntyFor/<string:room>')
api.add_resource(getAllTodaysDataForRoom,
                 '/allTodaysDataRoom/<string:room>/<int:allData>')
api.add_resource(getAllTodaysData, '/allTodaysData')
api.add_resource(getAllDataBaseData, '/allData')
api.add_resource(helloWorld, '/')


def runServer():
    log.info('Start flask API server as demon')
    app.run(host='0.0.0.0')
    db.databseColseConnect(database)
