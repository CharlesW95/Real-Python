# --- Flask Hello World --- #

# import the Flask class from the flask module

from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")

def hello_world():
	return "Hello, World?????!"

# dynamic routes

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/name/<name>")
def index(name):
	if name.lower()  == "michael":
		return "Hello {}".format(name), 200
	else:
		return "Not found", 404


# start the development server using the run() method
if __name__ == "__main__":
	app.run()