'''
Created on 28 Feb 2020

@author: Lisa Wehbrink
'''
from string import ascii_lowercase

class Booking(object):
    passenger_id = 0
    reference_no = ""
    flight_no = ""
    flight_date = ""

    def __init__(self, passenger_id, reference_no, flight_no, flight_date):
        self.passenger_id = passenger_id
        self.reference_no = reference_no
        self.flight_no = flight_no
        self.flight_date = flight_date


def create_Booking(passenger_id, reference_no, flight_no, flight_date):
    booking = Booking(passenger_id, reference_no, flight_no, flight_date)
    return booking

def generate_reference(first_name, last_name, flight_date, flight_no):
    
    letters = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
    n1 = letters[first_name[0].lower()]
    n2 = letters[last_name[0].lower()]
    
    n3 = flight_no
    
    n4 = str(flight_date).replace("-", "")
    
    reference_no = int(str(n1) + str(n2) + str(n3) + str(n4))
    
    return reference_no
