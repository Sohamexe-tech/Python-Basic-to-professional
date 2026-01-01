from bottle import*

application=Bottle()

@application.route("/")
def home():
	return template("home")

run(application, debug=True,use_reloader=True)