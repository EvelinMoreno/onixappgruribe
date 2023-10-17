import pandas as pd

from helpers.crearCSV import empleadosCSV
from data.empleados import empleados

 
empleadosCSV(empleados, 'empleados.csv')

#2. cargo la fuente de datos y con PANDAS creo un dataframe
EmpleadosDataFrame=pd.read_csv('data/empleados.csv')
print(EmpleadosDataFrame)
