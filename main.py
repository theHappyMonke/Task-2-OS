from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()