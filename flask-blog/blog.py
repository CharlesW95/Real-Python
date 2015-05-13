# blog.py - CONTROLLER

# imports

from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3
from functools import wraps

# Configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'
DEBUG = True

app = Flask(__name__)

# pulls in app configureation by looking for UPPERCASE variables

app.config.from_object(__name__)

# function used for connecting to the database

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# Test if user is logged in

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash("You need to log in first.")
			return redirect(url_for('login'))
	return wrap

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	# Check if password is correct
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password']!= app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again.'
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	# Render main page
	return render_template("login.html", error=error)

@app.route('/main')
@login_required
def main():
	g.db = connect_db()
	cur = g.db.execute('SELECT * FROM posts')
	posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template("main.html", posts=posts)

@app.route('/add', methods=['POST'])
@login_required
def add():
	title = request.form['title']
	post = request.form['post']
	if not title or not post:
		flash("All fields are required. Please try again.")
		return redirect(url_for('main'))
	else:
		g.db = connect_db()
		g.db.execute("INSERT INTO posts VALUES(?,?)", (title, post))
		g.db.commit()
		g.db.close()
		flash("New entry was successfully posted!")
		return redirect(url_for('main'))

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out.')
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run()

