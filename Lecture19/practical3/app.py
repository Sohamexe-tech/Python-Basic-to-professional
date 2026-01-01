from bottle import*
from datetime import*

application= Bottle()

@application.route("/")
def home():
	dt=datetime.now()
	hr=dt.hour
	if hr<12:
		msg="Good Morning"
	elif hr():
		msg:"Good Afternoon "
	else:
		msg:"Good Evening "
	return template("home",msg=msg)

run(application,debug=True,use_reloader=True)
	