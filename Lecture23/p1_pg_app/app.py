from bottle import * 
from random import choice 
application = Bottle() 

@application.route("/", method=["GET", "POST"]) 
def home(): 
	if request.method == "POST": 
		le = int(request.forms.get("le")) 
		uc = request.forms.get("uc") 
		di = request.forms.get("di") 
		sp = request.forms.get("sp") 

		text = "abcdefghijklmnopqrstuvwxyz" 
		if uc: 
			text = text + text.upper() 
		if di: 
			text = text + "0123456789"
		if sp: 
			text = text + ")(*&^%$#@!<>{}" 
		text = list(text) 
		pw = ""
		for i in range(1, le+1, 1): 
			pw = pw + choice(text)

		return template("home", msg=pw)
	else: 
		return template("home", msg="") 


 

 

#run(application, debug=True, use_reloader=True, port=4050)