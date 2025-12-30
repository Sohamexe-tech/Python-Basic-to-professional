import matplotlib.pyplot as plt

company=input("Enter the name of the Company: ")
promoter=float(input("enter prometers holding: "))
fii=float(input("Enter fii: "))
dii=float(input("Enter dii: "))
public=float(input("Enter public holding: "))

names=["prometers","fii","dii","public"]
holdings=[promoter,fii,dii,public]

plt.pie(holdings,labels=names,autopct="%2f",explode=[0,0,0,0.2])
plt.savefig(company+"pdf")
plt.show()