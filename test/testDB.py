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
        
    
    def testFlightSearch(self):
        d = '2020-12-24'
        origin = 'LHR'
        destination = 'HAJ'
        
        f = connection.search_flights(d, origin, destination)
        
        assert len(f) > 0
    
    
    def testCustomQuery(self):
        query = "SELECT * FROM flights"
        
        result = connection.run_custom_query(query)
        
        assert len(result) > 0
    
    
    def testPassengerRetrieval(self):
        first_name = "Matt"
        last_name = "Smith"
        dob = "1979-04-13"
        
        p = connection.retrieve_passenger(first_name, last_name, dob)
        
        assert p.first_name == "Matt" and p.last_name == "Smith"
        
    
    def testPassengerStorage(self):
        p = passenger.register("Rebecca", "Schmidt", "1993-06-30", "DE")
        
        connection.store_passenger(p)
        test = connection.retrieve_passenger("Rebecca", "Schmidt", "1993-06-30")
        
        assert test.nationality == "DE" and test.first_name == "Rebecca"
        
    
    def testBookingRetrieval(self):
        b = connection.retrieve_booking(131997620201224)
        
        assert b.passenger_id == 3 and b.flight_no == 976
        
        
    def testBookingRetrievalByPassenger(self):
        bookings = connection.retrieve_booking_by_passenger("Matt", "Smith", "1979-04-13")
        
        assert len(bookings) >= 1
        b = bookings[0]
        assert b.passenger_id == 3 and b.flight_no == 976
    
    
    def testBooking(self):
        success = connection.store_booking("Rebecca", "Schmidt", "1993-06-30", 989, "2020-05-18")
        
        assert success == True
        
    
    def testBookCount(self):
        result = connection.count_bookings()
        
        assert isinstance(result, int)
        
    def testPassengerCount(self):
        result = connection.count_customers()
        
        assert isinstance(result, int)
        
    def testFlightCount(self):
        result = connection.count_flights()
        
        assert isinstance(result, int)