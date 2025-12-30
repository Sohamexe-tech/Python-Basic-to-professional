import pandas as pd 
import matplotlib.pyplot as plt

data=pd.read_csv("SC.csv")
Days=data["Days"]
Sales=data["Sales"]

plt.figure(figsize=(10,5))
plt.bar(Days,Sales,width=0.5,color=["red","green","orange"])

plt.xlabel("Days")
plt.ylabel("Sales")

plt.title("Soham's Cafe Sales Data")
plt.show()