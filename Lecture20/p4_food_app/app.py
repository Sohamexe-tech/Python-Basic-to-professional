from bottle import *

application=Bottle()

@application.route("/", method=["GET", "POST"])
def home():
	if request.method=="POST":
		name=request.forms.get("name")
		food=request.forms.get("food")
		msg="Name: "+str(name)+" and you like"+ " "+str(food)+" " + " food"	
		return template("home", msg=msg)
	else:
		return template("home", msg="")

run(application, use_reloader=True, debug=True)
