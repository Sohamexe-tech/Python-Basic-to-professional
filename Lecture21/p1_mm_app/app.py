from bottle import Bottle, run, request, template
import requests

application = Bottle()

@application.route("/", method=["GET", "POST"])
def index():
    if request.method == "POST":
        url = "https://zenquotes.io/api/random"
        
        try:
            res = requests.get(url, timeout=5)
            data = res.json()[0]   # ✅ FIX HERE

            quote = data.get("q", "No quote found")
            author = data.get("a", "Unknown")

        except Exception as e:
            quote = f"Error: {e}"
            author = ""

        return template("index", msg=quote, author=author)

    return template("index", msg="", author="")

run(application, debug=True, use_reloader=True)