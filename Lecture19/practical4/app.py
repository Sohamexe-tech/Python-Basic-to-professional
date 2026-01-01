from bottle import *
from datetime import datetime

application = Bottle()

@application.route("/", method=["GET", "POST"])
def home():
	if request.method == "POST":
		name = request.forms.get("name")
		print(name)

		dt = datetime.now()
		hr = dt.hour

		if hr < 12:
			msg = "Good Morning " + name
		elif hr < 16:
			msg = "Good Afternoon " + name
		else:
			msg = "Good Evening " + name

		return template("home", msg=msg)
	else:
		return template("home", msg="")
run(application, debug=True, reloader=True,port=4051)
