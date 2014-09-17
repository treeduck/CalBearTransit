import sqlite3
import time
from euclid import findcloseststop
from flask import Flask, request, g, render_template, redirect

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello():
	return render_template('index2.html', loc=False)

@app.route("/contact")
def hi():
    return render_template('index3.html') 

@app.route("/api/cheep", methods=["POST"])
def receive_cheep():
    print(request.form)
    location = [float(i) for i in request.form['name'].split(",")] #TODO
    closest_stop = findcloseststop(location[0], location[1])
    return render_template('index2.html', loc=closest_stop)
    
if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', debug = True, port = 5000)
