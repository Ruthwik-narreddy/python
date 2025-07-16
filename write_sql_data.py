import pydoc
import pandas as pd
import mysql.connector
import csv

mydb = mysql.connector.connect(
    host ="localhost",
    username ="root",
    password ="Ruthwik@2761",
    database ="cars"

)
cursor = mydb.cursor()

filename = "/Users/ruthwiknarreddy/Downloads/used_cars_data.csv"
with open(filename,"r") as csvfile :
    csvreader = csv.reader(csvfile)
    a = next(csvreader)
    for row in csvreader:
        s_no = row[0]
        Name = row[1]
        Location = row[2]
        year = row[3]
        Kilometers_Driven = row[4]
        Fuel_Type = row[5]
        Transmission = row[6]
        Owner_Type = row[7]
        Mileage = row[8]
        Engine = row[9]
        Power = row[10]
        Seats = 0
        if row[11] != '':
            Seats = row[11]
        else:
            Seats = Seats
        New_Price = row[12]
        price =0
        if row[13] != '':
            price = row[13]
        else:
            price = price
        sql = ("Insert into used_cars_data2(s_no,Name,Location,year,Kilometers_Driven,Fuel_Type,Transmission,Owner_Type,"
               "Mileage,Engine,Power,Seats,New_Price,"
               "price) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

        values = (s_no,Name,Location,year,Kilometers_Driven,Fuel_Type,Transmission,Owner_Type,Mileage,Engine,Power,Seats,New_Price,price)

        cursor.execute(sql,values)
mydb.commit()
cursor.close()
mydb.close()






