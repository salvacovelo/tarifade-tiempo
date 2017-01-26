'''
Created on Jan 25, 2017

@author: Salvador Covelo 10-10164
'''
from datetime import datetime, date
import time


time1= datetime.strptime("25/1/2017 8:55", "%d/%m/%Y %H:%M")
time2= datetime.strptime("27/1/2017 8:55", "%d/%m/%Y %H:%M")
tiempoDeServicio=((time2-time1).total_seconds())
tarifa=2
def calcularPrecio(tarifa,tiempoDeServicio):
    
    if (tarifa<0):
        print ("ERROR la tarifa no puede ser menor a 0")
        exit() 
        pass
    else: 
        if((tiempoDeServicio/60)<15):
            print(tiempoDeServicio/60)

            print("ERROR no cumple el minimo de tiempo")
            exit()
        else:
            result=((tiempoDeServicio/3600)*tarifa)
            
    return result 

precio=calcularPrecio(tarifa,tiempoDeServicio)
print(precio)