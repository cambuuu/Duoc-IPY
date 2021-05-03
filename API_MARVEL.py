from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify


db_connect = create_engine('sqlite:///C:/Users/Ricardo/Desktop/bd')
app = Flask(__name__)
api = Api(app)


class GetNombre(Resource):
	def get(self):
		conn = db_connect.connect()
		query = conn.execute("select nombre from marvel")
		return {'Nombre':[i[0] for i in query.cursor.fetchall()]}

class GetDescripcion(Resource):
	def get(self):
		conn = db_connect.connect()
		query = conn.execute("select descripcion from marvel")
		return {'Descripcion':[i[0] for i in query.cursor.fetchall()]}

api.add_resource(GetNombre,'/GetNombre')
api.add_resource(GetDescripcion,'/GetDescripcion')

if __name__ == '__main__':
	app.run(port='5002')
