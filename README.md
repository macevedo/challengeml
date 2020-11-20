# challengeml

La aplicacion presenta una solucion para encontrar "anomalias" en un dump de datos.
Que representa una anomalia en un set de datos? Las respuestas pueden ser varias.
En este caso se analizaron 2 situaciones: 
  1- establecer un limite para lo que podria ser una activad normal. Ejemplo, que se produzcan mas de X operaciones.
  2- Analizar la variacion entre 1 dato y el subsiguiente y establecer un limite para dicha variacion.
     De este tipo de analisis se podrian desprender muchas comparaciones por ejemplo tomar datos de un dia, semana, mes
     para hacer las comparaciones.
Existen muchas otras formas de establecer las anomalias, pero en definitiva esto dependera de los datos analizados y las circunstancias.

La solucion a partir de la deteccion de anomalias envia el mensaje en formato json a una cola. "send.py" 
Para probar el funcioanmiento hay que iniciar "receive.py" antes de enviar los msjs, asi se podra corrobar que los mensajes con la informacion 
sustraida del dataframe se envia correctamente.

Los files con la solucion son main.py, metricas.py. 
Luego hay otros files con otros propositos, test.py y tambien genere un script para simular la generacion de datos en un filegenerator.py
Luego index.py fue una prueba para subir los datos a un site usando Flask y mostrandolos en una tabla html.
