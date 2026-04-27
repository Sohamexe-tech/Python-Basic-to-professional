import requests

try:
    url="http://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr"
    response = requests.get(url)
    data=response.json()
    print(data)
    amt=data["bitcoin"]["inr"]
    print(amt)
except Exception as e:
    print("Error:",e)