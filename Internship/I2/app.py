from bottle import Bottle, run, request, template
from datetime import datetime

app = Bottle()

def get_zodiac(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"


@app.route('/', method=['GET', 'POST'])
def index():
    zodiac = None
    error = None

    if request.method == 'POST':
        day = request.forms.get('day')
        month = request.forms.get('month')
        year = request.forms.get('year')

        # Check if inputs contain only digits
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            error = "Only numeric values are allowed. No letters or symbols."
        else:
            day = int(day)
            month = int(month)
            year = int(year)

            try:
                # Validate proper date (handles 31 Feb etc.)
                datetime(year, month, day)
                zodiac = get_zodiac(day, month)
            except ValueError:
                error = "Invalid date entered."

    return template('index', zodiac=zodiac, error=error)


run(app, host='localhost', port=8080, debug=True)
