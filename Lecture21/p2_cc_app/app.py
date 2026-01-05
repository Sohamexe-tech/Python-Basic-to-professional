from bottle import*
import requests

application=Bottle()

@application.route("/",method=["GET","POST"])
def index():
	if request.method=="POST":
		url="https://api.exchangerate-api.com/v4/latest/USD"
		res=requests.get(url)
		data=res.json()
		dollar=data["rates"]["INR"]
		amt=float(request.forms.get("amt"))
		inr=dollar*amt
		msg="₹"+str(round(inr,2))
		return template("index",msg=msg)
	else:
		return template("index",msg="")

run(application,debug=True,use_reloader=True)
