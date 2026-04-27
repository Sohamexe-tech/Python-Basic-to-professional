from bottle import *
import requests

app = Bottle()

@app.route("/", method=["GET"])
def quote():
    quote_text = ""
    author = ""

    try:
        url = "https://zenquotes.io/api/random"
        res = requests.get(url, timeout=5)
        data = res.json()

        quote_text = data[0]["q"]
        author = data[0]["a"]

    except requests.exceptions.RequestException:
        quote_text = "Believe in yourself. Every day is a new beginning."
        author = "Unknown"

    except (KeyError, IndexError, ValueError):
        quote_text = "Success is not final, failure is not fatal."
        author = "Winston Churchill"

    return template(
        "quote.tpl",
        quote=quote_text,
        author=author
    )

run(app, debug=True, port=4040)
