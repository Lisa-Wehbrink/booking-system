'''
Created on 28 Feb 2020

@author: Lisa Wehbrink
'''

from datetime import datetime

class Booking(object):
    passenger = ""
    reference = ""
    flight_no = 0
    date = datetime.now()

    def __init__(self, passenger, reference, flight_no, date):
        self.passenger = passenger
        self.reference = reference
        self.flight_no = flight_no
        self.date = date
        
    def __eq__(self, other):
        passengers = self.passenger == other.passenger
        date = self.date == other.date
        number = self.flight_no == other.flight_no
        
        if passengers and date and number:
            return True
        
        return False


def create_Booking(passenger, reference, flight_no, date):
    booking = Booking(passenger, reference, flight_no, date)
    return booking


bookings = []
next_id = 111


def book(passenger, flight_no, date):
    global next_id
    reference = passenger.first_name[0] + passenger.last_name[0] + str(flight_no) + str(next_id)
    
    booking = Booking(passenger, reference, flight_no, date)
    
    for b in bookings:
        if b == booking:
            return False
    
    bookings.append(booking)
    next_id += 1
    return True

