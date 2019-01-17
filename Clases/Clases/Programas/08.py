#!/usr/bin/python2.7
# _*_ coding: utf/8 _*_
'''Edwin Cardoso Tovar
3120803567
Taller De Herramientas Computacionales
(aqui va una descripcion del programa y lo que se hace.
De ahora en adelante tenemos que poner todo esto
'''
x = 10.5;y = 1.0/3;z = 15.3
#es como escribir:
#x=algo
#y=algo
#z=algo
# o x,y,z=10.5,1.0/3,15.3
H = """
El punto en R3 es:
(x,y,z)=(%.2f,%g,%G)
""" % (x,y,z)

print H
#para la forma de como quiero mis cocientes o puntos decimales tienen
#en el orden en que van las variables

G="""
El punto en R3 es:
(x,y,z)=({laX:.2f},{laY:g},{laZ:G}
"""
print G

import math as m
from math import sqrt
from math import sqrt as s
from math import *  # no se recomienda y es para importar todas las funciones desde math
x=16
x=input("Cual es el valor al que le quieres calcular\n" +
        "la raiz")
print "la raiz cuadrada de %.2f es %f" % (x,m.sqrt(x))
print sqrt (16.5)
print s(16.5)
