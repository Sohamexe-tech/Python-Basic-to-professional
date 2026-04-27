import requests

try:

    url="https://ipinfo.io/"
    response = requests.get(url)
    print(response)

    data = response.json()
    print(data)

    city=data["city"]
    print(city)

    loc=data["loc"]
    print(loc)

    info=loc.split(",")
    lat=info[0]
    lon=info[1]

    print("Latitude:",lat)
    print("Longitude:",lon) 
except Exception as e:
    print("Error:",e) 