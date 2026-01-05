from bottle import*
from sqlite3 import*

def db_setup():
	con=None
	try:
		con=connect("lang.db")
		sql="create table if not exists person(name text, language text)"
		cursor=con.cursor()
		cursor.execute(sql)
		con.commit()
	except Exception as e:
		print("issue",e)
	finally:
		if con is not None:
			con.close()

db_setup()

application=Bottle()

@application.route("/",method=["GET","POST"])
def home():
	con=None
	try:
		con.commit("lang.db")
		sql="select name, languages from person"
		cursor=con.cursor()
		cursor.execute(sql)
		data=cursor.fetchall()
		return template("home",msg=data)
	except Exception as e:
		print("issue",e)
	finally:
		if con is not None:
			con.close()
	
	return template("home",msg="")

@application.route("/language",method=["GET","POST"])
def language():
	if request.method=="POST":
		name=request.forms.get("name")
		py=request.forms.get("py")
		ja=request.forms.get("ja")
		js=request.forms.get("js")
		genai=request.forms.get("genai")

		language=""
		if py:
			language=language+"python"
		if ja:
			language=language+"Java"
		if js:
			language=language+"Javascript"
		if genai:
			language=language+"Gen AI"

		con = None
		try:
			con=connect("lang.db")
			sql="insert into person values(?,?)"
			cursor=con.cursor
			msg = "saved" 
			return template("language", msg=msg) 
		except Exception as e: 
			print("issue", e) 
			msg = "issue" + str(e) 
			return template("language", msg=msg) 
		finally: 
 
			if con is not None: 
				con.close() 
	else: 
		return template("language", msg="") 

run(application, debug=True, use_reloader=True, port=4050) 
 
 


		