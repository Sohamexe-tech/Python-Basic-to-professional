from bottle import *
import requests

application = Bottle()

@application.route("/", method=["GET", "POST"])
def index():
    msg = ""

    if request.method == "POST":
        try:
            amt = request.forms.get("amt")
            curr = request.forms.get("curr")

            if amt is None or amt.strip() == "":
                raise ValueError("Amount cannot be empty")

            if not amt.isdigit():
                raise ValueError("Enter whole number only")

            amt = int(amt)

            if amt <= 0:
                raise ValueError("Amount must be positive")

            url = "https://api.exchangerate-api.com/v4/latest/" + curr
            res = requests.get(url, timeout=5)

            if res.status_code != 200:
                raise Exception("API Error")

            data = res.json()

            if "rates" not in data or "INR" not in data["rates"]:
                raise Exception("Invalid API response")

            rate = data["rates"]["INR"]
            ans = amt / rate
            msg = str(round(ans, 2))

        except ValueError as ve:
            msg = str(ve)

        except requests.exceptions.RequestException:
            msg = "Network error. Try again later"

        except Exception:
            msg = "Something went wrong"

    return template("index", msg=msg)

run(application, debug=True, use_reloader=True)
