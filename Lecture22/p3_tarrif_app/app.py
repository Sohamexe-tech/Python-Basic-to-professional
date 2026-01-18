from bottle import *
import re

app = Bottle()

@app.route("/", method=["GET", "POST"])
def home():
    result = ""
    error = ""

    if request.method == "POST":
        country = request.forms.get("country")
        amount = request.forms.get("amount")

        try:
            if not country or country.strip() == "":
                raise Exception("Country name cannot be empty")

            if not re.match("^[A-Za-z ]+$", country):
                raise Exception("Country name must contain only alphabets")

            if not amount or amount.strip() == "":
                raise Exception("Amount cannot be empty")

            if not amount.isdigit():
                raise Exception("Amount must contain only numbers")

            amount = float(amount)
            country = country.strip().upper()

            tariff_rates = {
                "INDIA": 0.10,
                "USA": 0.05,
                "UK": 0.08,
                "JAPAN": 0.12,
                "CANADA": 0.07,
                "AUSTRALIA": 0.09
            }

            if country not in tariff_rates:
                raise Exception("Country not supported")

            tariff = amount * tariff_rates[country]

            result = f"Tariff from USA to {country.title()} is ${tariff:.2f}"

        except Exception as e:
            error = str(e)

    return template("home", result=result, error=error)

run(app, host="localhost", port=8080, debug=True)
