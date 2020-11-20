#!/usr/bin/python

import MySQLdb

# Open database connection
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

##################
## create table ##
##################
# Open database connection
db = MySQLdb.connect("localhost","root","qwe123.","challengeml" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS DATOSALERT")

# Create table as per requirement
sql = """CREATE TABLE DATOSALERT (
         SEQ  INT NOT NULL AUTO_INCREMENT KEY,
         TIMESTAMP  CHAR(11),
         DPM FLOAT)"""

cursor.execute(sql)

# disconnect from server
db.close()