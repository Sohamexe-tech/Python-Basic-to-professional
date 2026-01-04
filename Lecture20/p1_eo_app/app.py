from bottle import*

application=Bottle()

@application.route("/",method=["GET","POST"])
def home():
	if request.method=="POST":
		num=int(request.forms.get("num"))
		if num%2==0:
			msg="Number"+" "+str(num)+" " + "is Even"
		else:
			msg="Number"+" "+str(num)+" " + "is Odd"
		return template("home",msg=msg)
	else:
		return template("home",msg="")

run(application,debug=True,use_reloader=True)
