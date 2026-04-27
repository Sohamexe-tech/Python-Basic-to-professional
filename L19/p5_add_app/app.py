from bottle import *

application = Bottle()

@application.route("/", method=["GET", "POST"])
def home():
	if request.method == "POST":
		n1 = float(request.forms.get("n1"))
		n2 = float(request.forms.get("n2"))
		response = n1 + n2
		msg = "Result = " + str(round(response, 2))
		return template("home", msg=msg)
	else:
		return template("home", msg="")

run(application, debug=True, reloader=True, port=4000)
