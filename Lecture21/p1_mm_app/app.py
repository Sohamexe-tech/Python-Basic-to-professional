from bottle import*
import requests

application=Bottle()

@application.route("/",method=["GET","POST"])
def index():
	if request.method=="POST":
		url="https://quotes-api-self.vercel.app/quote"
		res = requests.get(url)
		data = res.json()                   
		quote=data["quote"]
		author=data["author"]
		return template("index",msg=quote,author=author)
	else:

		return template("index",msg="",author="")

run(application,debug=True,use_reloader=True)