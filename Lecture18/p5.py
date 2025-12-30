import matplotlib.pyplot as plt

names = ["prometer", "fii", "dii", "public"]
holdings = [50, 18, 22, 10]

plt.pie(holdings, labels=names, autopct="%1.1f%%")

plt.show()
