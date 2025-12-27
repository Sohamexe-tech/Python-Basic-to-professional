import requests

try:
    url="https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    print(response)
    print(response.status_code)

    data=response.json()
    print(data)

    DOLLAR=data["rates"]["INR"]
    print(DOLLAR)

    amt=float(input("Enter Amount in $:"))
    air=DOLLAR*amt
    print("₹",round(air,2),sep="")
except Exception as e:
    print("Error:",e)
