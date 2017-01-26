'''
Created on Jan 26, 2017

@author: ungluedsalva
'''
import unittest
from datetime import datetime

from tarifa import *
from tarifa.primermodulo import calcularPrecio
tarifa=2
class Prueba(unittest.TestCase):
    def test_tiemposervicio(self):
        
        time1= datetime.strptime("25/1/2017 8:55", "%d/%m/%Y %H:%M")
        time2= datetime.strptime("27/1/2017 8:55", "%d/%m/%Y %H:%M")
        time=[time1,time2]
        self.assertEqual(calcularPrecio(tarifa,time),96 , "ERROR el resultado no es el esperado")
        ########################################
    def test_tiempoMenorA15Min(self):
        time1= datetime.strptime("25/1/2017 8:15", "%d/%m/%Y %H:%M")
        time2= datetime.strptime("25/1/2017 8:20", "%d/%m/%Y %H:%M")
        time=[time1,time2]
        self.assertEqual(calcularPrecio(tarifa,time),None , "ERROR tiempo de servicio mayor a 15 minutos cuando es menor a 15 minutos")
        
    def test_tarifaMenorA0(self):
        tarifa=-2
        time1= datetime.strptime("25/1/2017 8:15", "%d/%m/%Y %H:%M")
        time2= datetime.strptime("25/1/2017 8:20", "%d/%m/%Y %H:%M")
        time=[time1,time2]
        self.assertEqual(calcularPrecio(tarifa,time),None , "ERROR tarifa mayor a 0 cuando es menor a 0 ")
        
    def test_tiemposervicio2(self):
        
        time1= datetime.strptime("25/1/2017 8:55", "%d/%m/%Y %H:%M")
        time2= datetime.strptime("29/1/2017 8:55", "%d/%m/%Y %H:%M")
        time=[time1,time2]
        self.assertEqual(calcularPrecio(tarifa,time),192 , "ERROR el resultado no es el esperado")
            
    def test_tiemposervicioMayorA7Dias(self):
        
        time1= datetime.strptime("25/1/2017 8:55", "%d/%m/%Y %H:%M")
        time2= datetime.strptime("22/2/2017 8:55", "%d/%m/%Y %H:%M")
        time=[time1,time2]
        self.assertEqual(calcularPrecio(tarifa,time),None , "ERROR el resultado no es el esperado")
                              
                
        

#tiempoDeServicio=((time2-time1).total_seconds())