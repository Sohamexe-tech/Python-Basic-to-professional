from bottle import *
from datetime import datetime
import re

application = Bottle()

@application.route("/", method=["GET", "POST"])
def home():
    msg = ""

    if request.method == "POST":
        try:
            name = request.forms.get("name")

            if not name or name.strip() == "":
                raise ValueError("Name cannot be empty")

            if not re.match("^[A-Za-z ]+$", name):
                raise ValueError("Name must contain only alphabets")

            dt = datetime.now()
            hr = dt.hour

            if hr < 12:
                msg = "Good Morning " + name
            elif hr < 16:
                msg = "Good Afternoon " + name
            else:
                msg = "Good Evening " + name

        except ValueError as e:
            msg = str(e)

        except Exception:
            msg = "Something went wrong"

    return template("home", msg=msg)

run(application, debug=True, reloader=True, port=4051)
