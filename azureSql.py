#***************************************************************#
#Developed By: Rahul Ramawat                                    #
#Version: 1.0                                                   #
#***************************************************************#

import csv
import pyodbc

'''
CREATE TABLE athletes
(
athlid VARCHAR(30),
athlname VARCHAR(30),
nationality VARCHAR(30),
sex VARCHAR(30),
dob VARCHAR(30),
height NUMERIC(13,8),
weight NUMERIC(13,8),
sport INT,
gold INT,
silver INT,
bronze INT)
'''

server = 'testingdbpoc.database.windows.net'
database = 'TestMySQl'
username = '*****'
password = '****'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#row = cursor.fetchone()

with open('C://AzureData//csvData//athletes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
                print("header rows")
                line_count += 1
        elif line_count >= 1:
                print(row[0],row[7])
                cursor.execute("INSERT INTO athletes(athlid,dob,height,weight,gold,silver,bronze) VALUES(${0},(${1}),${2},${3},${4},${5},(${6}))".format(str(row[0]),
                str(row[4]),float(row[5]),float(row[6]),int(row[8]),int(row[9]),int(row[10])))
                cnxn.commit()
                line_count += 1
                print("Insert Complete")