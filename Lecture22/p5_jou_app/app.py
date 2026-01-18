from bottle import *
import re

app = Bottle()

# Temporary task storage
tasks = []

@app.route("/", method=["GET", "POST"])
def home():
    error = ""
    message = ""

    if request.method == "POST":
        try:
            task = request.forms.get("task")

            if not task or task.strip() == "":
                raise Exception("Task cannot be empty")

            # Only alphabets and spaces allowed
            if not re.match("^[A-Za-z ]+$", task):
                raise Exception("Only alphabets and spaces are allowed")

            tasks.append(task.strip())
            message = "Task added successfully"

        except Exception as e:
            error = str(e)

    return template("home", tasks=tasks, error=error, message=message)



@app.route("/delete/<index:int>")
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    redirect("/")


run(app, host="localhost", port=8080, debug=True)
