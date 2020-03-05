'''
Created on 4 Mar 2020

@author: Lisa Wehbrink
'''
from flask import Flask, render_template, request
from data import connection

app = Flask(__name__)

@app.route("/")
def index():
    b = connection.count_bookings()
    f = connection.count_flights()
    c = connection.count_customers()
    
    return render_template('index.html', user='Lisa', bookings=b, flights=f, customers=c)

@app.route("/book")
def booksite():
    
    return render_template('book.html', user='Lisa')


@app.route("/cancel", methods = ['POST', 'GET'])
def cancel():
    
    if request.method == 'POST':
        if 'referencenumber' in request.form:
            refno = request.form.getlist('referencenumber')[0]
            
            if refno != "":
                b = []
                booking = connection.retrieve_booking(int(refno))
                if not booking == None:
                    b.append(booking)
            else:
                fname = request.form.getlist('firstname')[0]
                lname = request.form.getlist('lastname')[0]
                dob = request.form.getlist('dateofbirth')[0]
                
                if fname != "" and lname != "" and dob != "":
                    b = connection.retrieve_booking_by_passenger(fname, lname, dob)
                else:
                    b = []    
                    
            return render_template("cancel.html", 
                                   bookings = b, t = "submit", action="Action")
        
        else:
            reference_no = request.form.getlist('booking')[0]
            print(reference_no)
            
            booking = connection.retrieve_booking(reference_no)
            b = []
            b.append(booking)
            
            connection.delete_booking(reference_no)
            
            return render_template("cancel.html", bookings = b, 
                                   t = "hidden", action="Status", success="Cancelled")
    
    else:
        return render_template('cancel.html', t = "submit", action="Action")


@app.route("/display", methods = ['POST', 'GET'])
def display():
    if request.method == 'POST':
        refno = request.form.getlist('referencenumber')[0]
        
        if refno != "":
            b = []
            b.append(connection.retrieve_booking(int(refno)))
        else:
            fname = request.form.getlist('firstname')[0]
            lname = request.form.getlist('lastname')[0]
            dob = request.form.getlist('dateofbirth')[0]
            
            if fname != "" and lname != "" and dob != "":
                b = connection.retrieve_booking_by_passenger(fname, lname, dob)
            else:
                b = []    
                
        return render_template("display.html", bookings = b)
    
    
    else:
        return render_template('display.html')

@app.route("/stats")
def stats():
    
    return render_template('stats.html', user='Lisa')



if __name__ == "__main__":
    app.run()             