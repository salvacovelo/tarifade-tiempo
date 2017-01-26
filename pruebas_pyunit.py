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
        self.assertEqual(calcularPrecio(tarifa,time),95 , "bien hecho")
        ########################################
        time1= datetime.strptime("25/1/2017 8:55", "%d/%m/%Y %H:%M")
        time2= datetime.strptime("25/1/2017 8:59", "%d/%m/%Y %H:%M")
        time=[time1,time2]
        self.assertEqual(calcularPrecio(tarifa,time),None , "bien hecho")
        
        

#tiempoDeServicio=((time2-time1).total_seconds())