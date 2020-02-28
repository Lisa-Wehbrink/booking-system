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
        p = passenger.register("Matt", "Smith", "17/12/85", "Ireland")
        f = flight.initialise(987, "8/9/20", 300, "LHR", "HAJ")
        assert book.book(p, f) == True
    
    def testDuplicateBook(self):
        p = passenger.register("Brian", "Smith", "18/5/92", "UK")
        f = flight.initialise(979, "5/5/20", 300, "LHR", "HAJ")
        assert book.book(p, f) == True
        assert book.book(p, f) == False
    
    def testSuccessiveBook(self):
        p1 = passenger.register("Adam", "Smith", "29/2/80", "UK")
        p2 = passenger.register("Julia", "Smith", "31/5/79", "Germany")
        f = flight.initialise(977, "4/4/20", 350, "LHR", "TXL")
        assert book.book(p1, f) == True
        assert book.book(p2, f) == True
    
    def testFlightNumberDate(self):
        f1 = flight.initialise(899, "4/4/20", 300, "LHR", "FRA")
        f2 = flight.initialise(899, "5/4/20", 300, "LHR", "FRA")
        
        assert f1.date != f2.date
    
        