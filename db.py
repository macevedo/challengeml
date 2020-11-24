from sqlalchemy import create_engine


class DataBase:

    def conect_db(self):
        engine = create_engine("mysql://{user}:{pw}@localhost/{db}"
                               .format(user="root",
                               pw="qwe123.",
                               db="challengeml"))
        return engine

    def insert_metricas_db(self, metricas):
        engine = self.conect_db()

        metricas.to_sql('datosanomalos', con=engine, if_exists='append', chunksize=1000, index=False)