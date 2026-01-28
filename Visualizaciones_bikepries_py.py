import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("BikePrices.csv")

sns.histplot(data=df, x="Year")
plt.title("Distribución del año de fabricación")
plt.show()

sns.violinplot(data=df, x="Owner", y="Selling_Price")
plt.title("Precio de venta según número de dueños")
plt.show()
