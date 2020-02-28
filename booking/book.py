'''
Created on 28 Feb 2020

@author: Lisa Wehbrink
'''


class Booking(object):
    passenger = ""
    reference = ""
    flight = ""

    def __init__(self, passenger, reference, flight):
        self.passenger = passenger
        self.reference = reference
        self.flight = flight
        
    def __eq__(self, other):
        passengers = self.passenger == other.passenger
        flights = self.flight == other.flight
        
        if passengers and flights:
            return True
        
        return False


def create_Booking(passenger, reference, flight):
    booking = Booking(passenger, reference, flight)
    return booking


bookings = []
next_id = 111


def book(passenger, flight):
    global next_id
    reference = passenger.first_name[0] + passenger.last_name[0] + str(flight.flight_no) + str(next_id)
    
    booking = Booking(passenger, reference, flight)
    
    for b in bookings:
        if b == booking:
            return False
    
    bookings.append(booking)
    next_id += 1
    return True

