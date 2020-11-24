import pandas as pd


class Metricas():
    data = pd.read_csv("data/dataset.csv", names=['date', 'dpm'])
    df = pd.DataFrame(data)
    anomaliaMax = 2500
    anomaliaMin = 50
    dfanomalias = pd.DataFrame()

    def detectar_anomalias(self):
         self.dfanomalias = pd.DataFrame(self.df.loc[self.df['dpm'] > self.anomaliaMax])
         return self.dfanomalias
