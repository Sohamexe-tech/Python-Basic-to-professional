import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"C:\pythonK\L18\SCNEW.csv")


Days = data["Days"]
burger = data["burger"]
pizza = data["pizza"]


x = np.arange(len(Days))
width = 0.3


plt.figure(figsize=(10,5))
plt.bar(x, burger, width=width, label="Burger")
plt.bar(x + width, pizza, width=width, label="Pizza")


plt.xticks(x + width/2, Days)
plt.xlabel("Days")
plt.ylabel("Sales")

plt.title("Soham's Cafe Burger vs Pizza")
plt.legend(fontsize=12)



plt.tight_layout()
plt.show()
