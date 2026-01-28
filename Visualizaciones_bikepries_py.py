import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("BikePrices.csv")

#Eliminar los valores negativos en la columna Selling_Price
df = df[df["Selling_Price"] >= 0]

#Histograma de año de fabricación
sns.histplot(data=df, x="Year")
plt.title("Distribución del año de fabricación")
plt.show()

#Grafico de viol+in segun el numero de dueños y el precio
sns.violinplot(
    data=df,
    x="Owner",
    y="Selling_Price",
    palette="Set2")

plt.title("Precio de venta según número de dueños de la bicicleta")
plt.show()

#Grafico de dona para conocer la proporción de bicicletas por numero de dueño
brand_counts = df['Owner'].value_counts()
cmap = plt.colormaps["tab20c"]
fig, ax = plt.subplots()
ax.pie(
    brand_counts.values,
    labels=brand_counts.index,
    colors=cmap(range(len(brand_counts))),
    wedgeprops=dict(width=0.5))
ax.set_title("Distribución por numero de dueños")
plt.show()