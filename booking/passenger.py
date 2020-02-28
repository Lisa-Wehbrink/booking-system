'''
Created on 28 Feb 2020

@author: Lisa Wehbrink
'''
from datetime import datetime

class Passenger(object):
    first_name = ""
    last_name = ""
    dob = datetime.now()
    nationality = ""

    def __init__(self, first_name, last_name, dob, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        nationality = nationality
        
    def __eq__(self, other):
        names = self.first_name == other.first_name and self.last_name == other.last_name
        date = self.dob == other.dob
        
        if names and date:
            return True
        
        return False


def create_Passenger(first_name, last_name, dob, nationality):
    passenger = Passenger(first_name, last_name, dob, nationality)
    return passenger

passengers = []


def register(first_name, last_name, string_date, nationality):
    dob = datetime.strptime(string_date, '%d/%m/%y')
    
    p = Passenger(first_name, last_name, dob, nationality)
    
    for passenger in passengers:
        if passenger == p:
            return passenger
    
    passengers.append(p)
    return p