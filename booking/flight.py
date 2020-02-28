'''
Created on 28 Feb 2020

@author: Lisa Wehbrink
'''

from datetime import datetime

class Flight(object):
    flight_no = 0
    date = datetime.now()
    capacity = 0
    origin = ""
    destination = ""

    def __init__(self, flight_no, date, capacity, origin, destination):
        self.flight_no = flight_no
        self.date = date
        self.capacity = capacity
        self.origin = origin
        self.destination = destination
        
    def __eq__(self, other):
        if self.flight_no == other.flight_no and self.date == other.date:
            return True
        
        return False
    
def create_Flight(flight_no, date, capacity, origin, destination):
    flight = Flight(flight_no, date, capacity, origin, destination)
    return flight

flights = []

def initialise(flight_no, string_date, capacity, origin, destination):
    date = datetime.strptime(string_date, '%d/%m/%y')
    
    f = Flight(flight_no, date, capacity, origin, destination)
    
    for flight in flights:
        if f == flight:
            return Flight
    
    flights.append(f)
    return f