from bottle import*
import requests

application=Bottle()

@application.route("/",method=["GET","POST"])
def index():
	if request.method=="POST":
		curr= request.forms.get("curr")
		url="https://api.exchangerate-api.com/v4/latest/"+curr
		res=requests.get(url)
		data=res.json()
		RATE=data["rates"]["INR"]
		amt=float(request.forms.get("amt"))
		air=amt/RATE
		msg=str(round(air,2))
		return template("index",msg=msg)
	else:
		return template("index",msg="")

run(application,debug=True,use_reloader=True)
