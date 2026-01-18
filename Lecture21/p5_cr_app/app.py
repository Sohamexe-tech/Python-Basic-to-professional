from bottle import *
import re

app = Bottle()

# Temporary course storage
courses = []

@app.route("/", method=["GET", "POST"])
def home():
    error = ""
    message = ""

    if request.method == "POST":
        try:
            course = request.forms.get("course")
            status = request.forms.get("status")

            # Course name validation
            if not course or course.strip() == "":
                raise Exception("Course name cannot be empty")

            if not re.match("^[A-Za-z ]+$", course):
                raise Exception("Course name must contain only alphabets")

            # Status validation
            if not status or status.strip() == "":
                raise Exception("Course status is required")

            if status not in ["Ongoing", "Completed"]:
                raise Exception("Invalid course status")

            courses.append({
                "course": course.strip(),
                "status": status
            })

            message = "Course added successfully"

        except Exception as e:
            error = str(e)

    return template("home", courses=courses, error=error, message=message)


# Delete a specific course
@app.route("/delete/<index:int>")
def delete_course(index):
    if 0 <= index < len(courses):
        courses.pop(index)
    redirect("/")


run(app, host="localhost", port=8080, debug=True)
