import matplotlib.pyplot as plt

#data
months=["Jan","Feb","Mar","Apr","May","jun"]
sales=[120,135,150,170,160,180]


#code
plt.figure(figsize=(10,5))
plt.plot(months, sales, linewidth=30, color="Red", marker="*", markerfacecolor="Black", markersize=40)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Lenovo Laptop Sales")
plt.grid()
plt.savefig("Lenovo.pdf")
plt.savefig("Lenovo.png")
plt.show()