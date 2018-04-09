from flask import Flask, redirect, render_template, request
from random import randint

app = Flask(__name__)


'''
@app.route('/')
def index():
	return 'Flask App!'

@app.route("/user/")
def hello():
	users = ['Alice', 'Steve', 'Alice', 'Bruce']

	return render_template('user.html', **locals())
'''

from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
app = Flask(__name__)
 
@app.route("/")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)
 

if __name__ == '__main__':
	app.run(debug = True)


