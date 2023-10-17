import pandas as pd

from helpers.crearCSV import crearCSV
from data.ventas import ventas

#1. crear csv con los datos de la ventas
crearCSV(ventas,'ventas.csv') 

#2. cargo la fuente de datos y con PANDAS creo un dataframe
ventasDataFrame=pd.read_csv('data/ventas.csv')

#3. Explorar los datos
examen1=ventasDataFrame.head()
examen2=ventasDataFrame.tail()
examen3=ventasDataFrame.head(20)
examen4=ventasDataFrame.info()
examen5=ventasDataFrame.describe()
examen6=ventasDataFrame.tail(50)


#4. Filtrar y otdenar(limpiar)

#5. Modelar o aplicar modelos

#6. Presentar y exportar los datos
print(examen1)
print("\n")
print(examen2)
print("\n")
print(examen3)
print("\n")
print(examen4)
print("\n")
print(examen5)
print("\n")
print(examen6)
print("\n")
