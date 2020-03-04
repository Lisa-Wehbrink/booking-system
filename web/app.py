'''
Created on 4 Mar 2020

@author: Lisa Wehbrink
'''
from flask import Flask, render_template
from data import connection

app = Flask(__name__)

@app.route("/")
def index():
    b = connection.count_bookings()
    f = connection.count_flights()
    c = connection.count_customers()
    
    return render_template('index.html', user='Lisa', bookings=b, flights=f, customers=c)

if __name__ == "__main__":
    app.run()             