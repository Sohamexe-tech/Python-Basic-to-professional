import requests

try:
    lattitude = (input("Enter the lattitude: "))
    longitude = (input("Enter the longitude: "))
    url = f"https://api.open-meteo.com/v1/forecast"
    
    response=requests.get(url,params={"latitude:":lattitude,"longitude":longitude,"current_weather":True})
    print(response)

    data=response.json()
    print(data)

    temp=data["current_weather"]["temperature"]
    print("Temperature:",temp)
except Exception as e:
    print("Error:",e)