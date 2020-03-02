'''
Created on 28 Feb 2020

@author: Lisa Wehbrink
'''
import unittest
from booking import book
from booking import passenger
from booking import flight

class TestBook(unittest.TestCase):

    def testFirstBook(self):
        p = passenger.register("Matt", "Smith", "1985-12-17", "Ireland")
        f = flight.initialise(987, "2020-09-08", "8:05:00", "10:30:00", 300, "LHR", "HAJ")
        assert book.book(p, f) == True
    
    def testSuccessiveBook(self):
        p1 = passenger.register("Adam", "Smith", "1980-02-29", "UK")
        p2 = passenger.register("Julia", "Smith", "1979-05-31", "Germany")
        f = flight.initialise(977, "2020-04-04", "14:40:00", "16:30:00", 350, "LHR", "TXL")
        assert book.book(p1, f) == True
        assert book.book(p2, f) == True
    
    def testFlightNumberDate(self):
        f1 = flight.initialise(899, "2020-04-04", "15:55:00", "18:30:00", 300, "LHR", "FRA")
        f2 = flight.initialise(899, "2020-04-05", "15:55:00", "18:30:00", 300, "LHR", "FRA")
        
        assert f1.date != f2.date
    
        