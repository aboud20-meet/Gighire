from flask import Flask, flash,send_from_directory, render_template, url_for,redirect, request ,jsonify, session  as flask_session

from databases import *


app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/', methods=['GET','POST'])
def homepage():
	if request.method == "POST":
		return render_template('gighire.html')
	else:
		return render_template('signup.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def user_signUp():
	return render_template("gighire.html")

@app.route('/apply',methods=['GET','POST'])
def apply():
	if request.method == 'GET':
		return render_template("apply.html")

@app.route('/profile',methods=['GET','POST'])
def profile():
	if request.method == 'GET':
		return render_template("profile.html")







if __name__ == "__main__":
	app.run(debug=True)
