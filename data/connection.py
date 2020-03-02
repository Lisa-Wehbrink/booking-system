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

def retrieve_passenger(first_name, last_name, dob):
    connect()
    
    query = "SELECT * FROM passengers WHERE first_name = '" + first_name + "' "
    query += " AND last_name = '" + last_name + "'"
    query += " AND date_of_birth = '" + str(dob) + "'"
    
    cur = db.cursor()
    cur.execute(query)
    
    row = cur.fetchone()
    p = passenger.register(row[1], row[2], str(row[3]), row[4])
    disconnect()
   
    return p


def store_passenger(p):
    query = "INSERT INTO passengers (first_name, last_name, date_of_birth, nationality)"
    query += "VALUES (%a, %b, %c, %d) "
    query += "ON DUPLICATE KEY UPDATE first_name=%a"
    
    query = query.replace("%a", ("'" + p.first_name + "'"))
    query = query.replace("%b", ("'" + p.last_name + "'"))
    query = query.replace("%c", ("'" + str(p.dob) + "'"))
    query = query.replace("%d", ("'" + p.nationality + "'"))

    connect()
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    
    disconnect()
    
    
def retrieve_booking(reference_no):
    connect()
    
    query = "SELECT * FROM bookings WHERE reference_no = " + str(reference_no)
    
    cur = db.cursor()
    cur.execute(query)
    
    row = cur.fetchone()
    b = book.create_Booking(row[1], row[0], row[2], row[3])
    disconnect()
   
    return b


def retrieve_booking_by_passenger(first_name, last_name, dob):
    query = """SELECT b.customer_id, reference_no, flight_no, flight_date 
            FROM passengers p INNER JOIN bookings b 
            ON p.customer_id = b.customer_id WHERE first_name = '"""
    query += first_name + "' and last_name = '" + last_name + "'"
    query += " AND date_of_birth = '" + str(dob) + "'"

    connect()
    cur = db.cursor()
    cur.execute(query)
    
    bookings = []
    
    for row in cur.fetchall():
        b = book.create_Booking(row[0], row[1], row[2], row[3])
        bookings.append(b)
    
    db.close()
    return bookings


def store_booking(first_name, last_name, dob, flight_no, flight_date):
    cid_query = "SELECT customer_id FROM passengers WHERE first_name = '"
    cid_query += first_name + "' AND last_name = '" + last_name + "'"
    cid_query += " AND date_of_birth = '" + str(dob) + "'"
    
    f_query = "SELECT COUNT(*) FROM flights WHERE flight_no = " + str(flight_no)
    f_query += " AND flight_date = '" + str(flight_date) + "'"
    
    query = "INSERT INTO bookings (reference_no, customer_id, flight_no, flight_date) "
    query += "VALUES (%a, %b, %c, %d)"
    query += " ON DUPLICATE KEY UPDATE reference_no=%a"
    
    connect()
    cur = db.cursor()
    
    cur.execute(cid_query)
    cid = cur.fetchone()[0]
    
    cur.execute(f_query)
    if not cur.fetchone():
        return False
    
    reference_no = book.generate_reference(first_name, last_name, flight_date, flight_no)

    query = query.replace("%a", str(reference_no))
    query = query.replace("%b", str(cid))
    query = query.replace("%c", str(flight_no))
    query = query.replace("%d", ("'" + str(flight_date) + "'"))

    cur.execute(query)
    return True