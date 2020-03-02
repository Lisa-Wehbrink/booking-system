'''
Created on 2 Mar 2020

@author: Lisa Wehbrink
'''
import unittest
from booking import book
from booking import passenger
from booking import flight
from data import connection

class TestBook(unittest.TestCase):
    
    def testFlightRetrieval(self):
        flight_no = 976
        flight_date = "\'2020-12-24\'"
        f = connection.retrieve_flight(flight_no, flight_date)
        
        assert f.capacity == 300 and f.origin == "LHR" and f.destination == "HAJ"
    
    
    def testFlightStorage(self):
        f = flight.initialise(989, "2020-05-18", "15:55:00", "18:30:00", 300, "LHR", "HAJ")
        
        connection.store_flight(f)
        test = connection.retrieve_flight(989, "'2020-05-18'")
        
        assert test.flight_no == 989
    
    
    def testCustomQuery(self):
        query = "SELECT * FROM flights"
        
        result = connection.run_custom_query(query)
        
        assert len(result) > 0
    