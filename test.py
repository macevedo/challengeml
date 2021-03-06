import pandas as pd
import MySQLdb

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
            diferencia = (registro1/registro2)-1
            if diferencia < 0: diferencia = diferencia * -1
            diferencia = round(diferencia, 2)
            j = j+1
            i = i+1
            if(diferencia > 0.1):
                print("la diferencia porcentual entre "+str(registro1)+" y "+str(registro2) +" es de "+str(diferencia))


""""
df2 = pd.DataFrame({'uno': [1, 2, 3], 'dos': [4, 5, 6], 'tres': [7, 8, 9]}, index=['x', 'y', 'z'])
# Iteración por filas del DataFrame:
for indice_fila, fila in df2.iterrows():
	print(indice_fila)
	print(fila)
"""

test1 = Tests()
#print(Tests.testDetectarAnomalias(test1))
##print(Tests.testDataframeToJson(test1))
#rint(Tests.testDiferenciaPorRegistro(test1))
df = Tests.testDetectarAnomalias(test1)
##insert
##
db = MySQLdb.connect("localhost","root","qwe123.","challengeml" )
cursor = db.cursor()

cols = "`,`".join([str(i) for i in Tests.testDetectarAnomalias(test1).columns.tolist()])

#print(df)

for row in df.iterrows():
    sql = "INSERT INTO `DATOSALERT` (`" + cols + "`) VALUES (" + "%s," * (len(row) - 1) + "%s)"

#Test conecction dB
db = MySQLdb.connect("localhost","root","qwe123.","challengeml" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)
# disconnect from server
db.close()