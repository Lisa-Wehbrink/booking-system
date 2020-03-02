'''
Created on 2 Mar 2020

@author: Lisa Wehbrink
'''
import mysql.connector as mysql
from mysql.connector import Error
from booking import book
from booking import passenger
from booking import flight


def connect():
    global db
    try:
        db =mysql.connect(
          host="localhost",
          user="root",
          passwd="G-D/F#-e-D/F#-Gmaj7",
          db = "booking_engine"
        )
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (db.is_connected()):
            print("Connection established.")
    
    
def disconnect():
    db.close()
    print("Connection closed.")


def run_custom_query(query):
    connect()
    
    cur = db.cursor()
    cur.execute(query)
    
    result = []
    
    for row in cur.fetchall():
        result.append(row)
        
    return result


def retrieve_flight(number, flight_date):
    connect()
    
    query = "SELECT * FROM flights WHERE flight_no = " + str(number)
    query += " AND flight_date = " + flight_date
    
    cur = db.cursor()
    cur.execute(query)
    
    row = cur.fetchone()
    f = flight.initialise(row[0], str(row[1]), str(row[2]), str(row[3]), row[6], row[4], row[5])
    disconnect()
   
    return f


def store_flight(f):
    query = "INSERT INTO flights (flight_no, flight_date, dep_time, arr_time"
    query += ", origin, destination, capacity) "
    query += "VALUES (%a, %b, %c, %d, %e, %f, %g) "
    query += "ON DUPLICATE KEY UPDATE flight_no=%a"
    
    query = query.replace("%a", str(f.flight_no))
    query = query.replace("%b", ("'" + str(f.date) + "'"))
    query = query.replace("%c", ("'" + str(f.dep_time) + "'"))
    query = query.replace("%d", ("'" + str(f.arr_time) + "'"))
    query = query.replace("%e", ("'" + f.origin + "'"))
    query = query.replace("%f", ("'" + f.destination + "'"))
    query = query.replace("%g", str(f.capacity))
        
    connect()
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    
    disconnect()
    