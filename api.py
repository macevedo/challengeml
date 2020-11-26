from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine, MetaData, Table, Column, String
from sqlalchemy.orm import Session, mapper
import json


app = Flask(__name__)
api = Api(app)

class Datos(object):
    def __init__(self, date, dpm):
        self.date = date
        self.dpm = dpm


class DatosAnomalos(Resource):

    def get(self):
        engine = create_engine("mysql://{user}:{pw}@localhost/{db}"
                               .format(user="root",
                                       pw="qwe123.",
                                       db="challengeml"))

        metadata = MetaData()

        metricasml = Table("datosanomalos", metadata,
                           Column('date', String, primary_key=True),
                           Column('dpm', String, nullable=False)
                           )

        mapper(Datos, metricasml)
        session = Session(engine)
        my_list = list(session.query(metricasml))
        json_data = json.dumps(my_list)

        return json_data


api.add_resource(DatosAnomalos, '/datos')

if __name__ == '__main__':
    app.run(debug=True)