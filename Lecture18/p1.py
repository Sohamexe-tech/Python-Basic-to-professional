import pandas as pd 
import matplotlib.pyplot as plt

data=pd.read_csv("TCS.csv")
Month=data["Month"]
Price=data["Price"]

plt.figure(figsize=(10,5))
plt.plot(Month,Price,linewidth=10,marker="o",markersize=20,markerfacecolor="black")

plt.xlabel("Months")
plt.ylabel("Price")

plt.title("TCS Stock Price")
plt.grid()

plt.savefig("tcs.pdf")
plt.savefig("tcs.png")

plt.show()