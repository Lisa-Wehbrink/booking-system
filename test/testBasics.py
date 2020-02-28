'''
Created on 28 Feb 2020

@author: Lisa Wehbrink
'''
import unittest
from datetime import datetime
from booking import book
from booking import passenger

class TestBook(unittest.TestCase):

    def testFirstBook(self):
        date = datetime.strptime("8/9/20", '%d/%m/%y')
        p = passenger.Passenger("Matt", "Smith", "9/6/85", "Ireland")
        assert book.book(p, 987, date) == True
    
    def testDuplicateBook(self):
        date = datetime.strptime("8/9/20", '%d/%m/%y')
        p = passenger.Passenger("Brian", "Smith", "18/5/92", "UK")
        assert book.book(p, 987, date) == True
        assert book.book(p, 987, date) == False
    
    def testSuccessiveBook(self):
        date = datetime.strptime("8/9/20", '%d/%m/%y')
        p1 = passenger.Passenger("Adam", "Smith", "29/2/80", "UK")
        p2 = passenger.Passenger("Julia", "Smith", "31/5/79", "Germany")
        assert book.book(p1, 987, date) == True
        assert book.book(p2, 987, date) == True
    
        