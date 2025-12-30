import pandas as pd 
import matplotlib.pyplot as plt

data=pd.read_csv("TI.csv")
Month=data["Month"]
TCS=data["TCS"]
Infy=data["Infy"]

plt.figure(figsize=(14,6))

plt.plot(Month,TCS,linewidth=5,marker="o",markersize=20,markerfacecolor="black",label="TCS")
plt.plot(Month,Infy,linewidth=5,marker="s",markersize=20,markerfacecolor="Black",label="Infosys")

plt.xlabel("Months")
plt.ylabel("Price")

plt.title("TCS VS Infosys \n Stock Price")

plt.grid()

plt.legend(fontsize=20,shadow=True,loc="center right")

plt.show()