from bottle import*


application=Bottle()

@application.route("/")
def home():
	return template("home")

run(application,use_reloader=True,debug=True)