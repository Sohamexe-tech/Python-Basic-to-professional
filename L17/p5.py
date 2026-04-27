import requests 

def gr(currency):
	try:
		url="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies="+curr
		res=requests.get(url)
		data=res.json()
		print(data)
		amt=data["bitcoin"][curr]
		print(amt)
	except Exception as e:
		print("issue", e)

while True:
	op=int(input("1 inr, 2 usd, 3 eur, 4 sgd, 5 aud, and 6 exit: \n"))
	if op==1:
		curr="inr"
		gr(curr)
	elif op==2:
		curr="usd"
		gr(curr)
	elif op==3:
		curr="eur"
		gr(curr)
	elif op==4:
		curr="sgd"
		gr(curr)
	elif op==5:
		curr="aud"
		gr(curr)
	elif op==6:
		break
	else:
		print("invalid option")