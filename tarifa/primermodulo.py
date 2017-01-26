'''
Created on Jan 25, 2017

@author: Salvador Covelo 10-10164
'''
from datetime import datetime
import time


#time1= datetime.strptime("25/1/2017 8:55", "%d/%m/%Y %H:%M")
#time2= datetime.strptime("25/1/2017 8:59", "%d/%m/%Y %H:%M")
#tiempoDeServicio=[time1,time2]

#tiempoDeServicio=((time2-time1).total_seconds())
#tarifa=2
def calcularPrecio(tarifa,tiempoDeServicio):
    tiempototal=(tiempoDeServicio[1]-tiempoDeServicio[0]).total_seconds()
    if (tarifa<0):
        print ("ERROR la tarifa no puede ser menor a 0")
        return None 
        
    else: 
        if((tiempototal/60)<15):
            #print(tiempototal/60)

            print("ERROR no cumple el minimo de tiempo")
            return None
        else:
            if ((tiempototal/3600)>24*7):
                print("ERROR tranajo mas de 7 dias")
                return None
            else:
                result=((tiempototal/3600)*tarifa)
            
    return result 
