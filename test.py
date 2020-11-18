import pandas as pd

#testdataset.csv tiene 100 lineas.

class Tests():
    data = pd.read_csv("data/testdataset.csv", names=['date', 'dpm'],index_col=False)
    df = pd.DataFrame(data)
    anomaliaMax = 800

# La prueba debe devolver el resultado segun la anomaliaMax establecida
    def testDetectarAnomalias(self):
        dfanomalias = pd.DataFrame(self.df.loc[self.df['dpm'] > self.anomaliaMax])
        return dfanomalias

#Convierte el DataFrame en un json para enviar como msj o utilizar por una API
    def testDataframeToJson(self):
        dfjson = self.testDetectarAnomalias().to_json(index=False,orient='split')
        return dfjson

    def testDiferenciaPorRegistro(self):
        i = 0
        j = 1

        while j < 100:
            registro1 = self.df.dpm[i]
            registro2 = self.df.dpm[j]
            #print(registro1)
            #print(registro2)
            diferencia = (registro1/registro2)-1
            if diferencia < 0: diferencia = diferencia * -1
            diferencia = round(diferencia, 2)
            #print(diferencia)
            j = j+1
            i = i+1
            #print(j)
            #print(i)
            if(diferencia > 0.1):
                print("la diferencia porcentual entre "+str(registro1)+" y "+str(registro2) +" es de "+str(diferencia))


test1 = Tests()
print(Tests.testDetectarAnomalias(test1))
print(Tests.testDetectarAnomalias(test1).count())
print(Tests.testDataframeToJson(test1))
print(Tests.testDiferenciaPorRegistro(test1))