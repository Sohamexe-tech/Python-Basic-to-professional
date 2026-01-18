from bottle import *
import math

app = Bottle()

@app.route("/", method=["GET", "POST"])
def home():
    result = ""
    error = ""

    if request.method == "POST":
        try:
            operation = request.forms.get("operation")
            n1 = request.forms.get("n1")
            n2 = request.forms.get("n2")

            if not operation:
                raise Exception("Please select an operation")

            if not n1 or n1.strip() == "":
                raise Exception("First value cannot be empty")

            n1 = float(n1)

            if operation != "bmi":
                if not n2 or n2.strip() == "":
                    raise Exception("Second value cannot be empty")
                n2 = float(n2)

            if operation == "add":
                result = f"Result: {n1 + n2}"

            elif operation == "sub":
                result = f"Result: {n1 - n2}"

            elif operation == "mul":
                result = f"Result: {n1 * n2}"

            elif operation == "div":
                if n2 == 0:
                    raise Exception("Division by zero is not allowed")
                result = f"Result: {n1 / n2:.2f}"

            elif operation == "bmi":
                height = n1 / 100  # cm to meter
                bmi = n2 = float(request.forms.get("n2"))
                bmi_value = bmi / (height ** 2)
                result = f"BMI: {bmi_value:.2f}"

            else:
                raise Exception("Invalid operation selected")

        except ValueError:
            error = "Please enter valid numeric values"
        except Exception as e:
            error = str(e)

    return template("home", result=result, error=error)

run(app, host="localhost", port=8080, debug=True)
