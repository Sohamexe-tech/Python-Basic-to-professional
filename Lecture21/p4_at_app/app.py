from bottle import *
import re

app = Bottle()

# Temporary attendance storage
records = []

@app.route("/", method=["GET", "POST"])
def home():
    error = ""
    message = ""

    if request.method == "POST":
        try:
            name = request.forms.get("name")
            status = request.forms.get("status")

            # Name validation
            if not name or name.strip() == "":
                raise Exception("Student name cannot be empty")

            if not re.match("^[A-Za-z ]+$", name):
                raise Exception("Student name must contain only alphabets")

            # Status validation
            if not status or status.strip() == "":
                raise Exception("Attendance status is required")

            if status not in ["Present", "Absent"]:
                raise Exception("Invalid attendance value")

            records.append({
                "name": name.strip(),
                "status": status
            })

            message = "Attendance recorded successfully"

        except Exception as e:
            error = str(e)

    return template("home", records=records, error=error, message=message)


# Delete a specific record
@app.route("/delete/<index:int>")
def delete_record(index):
    if 0 <= index < len(records):
        records.pop(index)
    redirect("/")


run(app, host="localhost", port=8080, debug=True)
