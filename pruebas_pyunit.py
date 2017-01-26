'''
Created on Jan 26, 2017

@author: ungluedsalva
'''
import unittest
from datetime import datetime

from tarifa import *
from tarifa.primermodulo import calcularPrecio

class Prueba(unittest.TestCase):
    def test_tiemposervicio(self):
        tarifa=2
        time1= datetime.strptime("25/1/2017 8:55", "%d/%m/%Y %H:%M")
        time2= datetime.strptime("27/1/2017 8:55", "%d/%m/%Y %H:%M")
        time=[time1,time2]
        self.assertEqual(calcularPrecio(tarifa,time),96 , "ERROR el resultado no es el esperado")
        ########################################
        time1= datetime.strptime("25/1/2017 8:15", "%d/%m/%Y %H:%M")
        time2= datetime.strptime("25/1/2017 8:20", "%d/%m/%Y %H:%M")
        time=[time1,time2]
        self.assertEqual(calcularPrecio(tarifa,time),None , "ERROR tiempo de servicio mayor a 15 minutos cuando es menor a 15 minutos")
        
        
        

#tiempoDeServicio=((time2-time1).total_seconds())