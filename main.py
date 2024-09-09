from flask import Flask, render_template
import sqlite3


'''################# Database content #################'''

connection = sqlite3.connect('Bean&Brew.db', check_same_thread = False)

cursor = connection.cursor()

query = """CREATE TABLE IF NOT EXISTS
users(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
password TEXT NOT NULL)"""

cursor.execute(query)
#cursor.execute("INSERT INTO users VALUES (NULL, ?, ?, ?), (?, 'admin', 'admin@Bean&Brew.com', 'admin')")
#cursor.execute("SELECT * FROM users")
#connection.commit()
cursor.close()

'''################# Flask content #################'''

#Flask app instance
app = Flask(__name__)

#Flask app routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/booking/tables')
def table():
    return render_template('table-booking.html')

@app.route('/booking/classes')
def classes():
    return render_template('class-booking.html')

@app.route('/sign-in')
def sign_in():
    return render_template('sign-in.html')

#Runs flask in debug mode
if __name__ == '__main__':
    app.run(debug = True)