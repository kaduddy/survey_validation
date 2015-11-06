from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
	return render_template("index.html")
@app.route('/submit', methods = ['POST'])
def process():
	if len(request.form['name']) < 1:
		flash("Name cannot be empty!")
		return redirect('/')
	elif len(request.form['comment']) < 1:
		flash("Please enter a comment!")
		return
	elif len(request.form['comment']) > 120:
		flash("Please limit your comment to 120 characters")		
	else:
		session['name'] = request.form['name']
		session['location'] = request.form['location']
		session['language'] = request.form['language']
		session['comment'] = request.form['comment']
	return redirect ('/result')
	
@app.route('/result')
def result():
	return render_template("result.html")

app.run(debug=True)

#the name and comment fields should be validated
#so they are not blank
#validate that the comment field is no longer
#than 120 characters