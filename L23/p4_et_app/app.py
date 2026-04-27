from bottle import *
import re

app = Bottle()

# Temporary storage
expenses = []

@app.route("/", method=["GET", "POST"])
def home():
    error = ""
    message = ""

    if request.method == "POST":
        try:
            day = request.forms.get("day")
            amount = request.forms.get("amount")
            categories = request.forms.getall("category")

            # Day validation
            if not day or day.strip() == "":
                raise Exception("Day cannot be empty")

            if not re.match("^[A-Za-z ]+$", day):
                raise Exception("Day must contain only alphabets")

            # Amount validation
            if not amount or amount.strip() == "":
                raise Exception("Amount cannot be empty")

            if not amount.isdigit():
                raise Exception("Amount must contain only numbers")

            amount = float(amount)

            # Category validation (multiple allowed)
            if not categories:
                raise Exception("Select at least one category")

            expenses.append({
                "day": day.strip(),
                "amount": amount,
                "categories": ", ".join(categories)
            })

            message = "Expense added successfully"

        except Exception as e:
            error = str(e)

    return template("home", expenses=expenses, error=error, message=message)


@app.route("/delete/<index:int>")
def delete_expense(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)
    redirect("/")


run(app, host="localhost", port=8080, debug=True)
