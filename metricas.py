import pandas as pd
import pika


class Metricas():
    data = pd.read_csv("data/dataset.csv", names=['date', 'dpm'])
    df = pd.DataFrame(data)
    anomaliaMax = 2500
    anomaliaMin = 50
    dfanomalias = pd.DataFrame()

    def detectarAnomalias(self):
         self.dfanomalias = pd.DataFrame(self.df.loc[self.df['dpm'] > self.anomaliaMax])
         return self.dfanomalias

    def DataframeToJson(self, dfanomalias):
        dfjson = pd.DataFrame()(index=False,orient='split')
        return self.dfjson

    def diferenciaPorRegistro(self):
        i = 0
        j = 1

        while (j < 100):
            registro1 = self.df.dpm[i]
            registro2 = self.df.dpm[j]
            diferencia = (registro1 / registro2) - 1
            j = j + 1
            i = i + 1
            if (diferencia > 0.1):
                print("la diferencia porcentual entre " + str(registro1) + " y " + str(registro2) + "es de " + str(
                    diferencia[:4]))


    def sendMessage(self):

        msg = self.detectarAnomalias().to_json(index=False, orient='split')

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        channel.basic_publish(exchange='', routing_key='hello', body=str(msg))
        print(" [x] Sent " + str(msg))
        connection.close()



#def diferenciaDiaria():
#    sumadiaria = 0
#    i = 0
#    for row in df.iterrows():

