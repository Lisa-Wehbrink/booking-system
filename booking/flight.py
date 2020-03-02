'''
Created on 28 Feb 2020

@author: Lisa Wehbrink
'''

from datetime import datetime
from datetime import time

class Flight(object):
    flight_no = 0
    date = datetime.now()
    dep_time = ""
    arr_time = ""
    capacity = 0
    origin = ""
    destination = ""
    

    def __init__(self, flight_no, date, dep_time, arr_time, capacity, origin, destination):
        self.flight_no = flight_no
        self.date = date
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.capacity = capacity
        self.origin = origin
        self.destination = destination
        
    def __eq__(self, other):
        if self.flight_no == other.flight_no and self.date == other.date:
            return True
        
        return False
    
def create_Flight(flight_no, date, dep_time, arr_time, capacity, origin, destination):
    flight = Flight(flight_no, date, dep_time, arr_time, capacity, origin, destination)
    return flight


def initialise(flight_no, string_date, string_dep, string_arr, capacity, origin, destination):
    date = datetime.strptime(string_date, '%Y-%m-%d')
    dep_time = datetime.strptime(string_dep, '%H:%M:%S').time()
    arr_time = datetime.strptime(string_arr, '%H:%M:%S').time()
    
    return Flight(flight_no, date, dep_time, arr_time, capacity, origin, destination)

