#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"Convertir de grados Celsius a Fahrenheit y de grados Fahrenheit a Celsius"

n=int(input("Seleccione Conversion\n1. ºC a ºF\n2. ºF a ºC\n" ))

def Conversion():
    if(n==1):
        c= float(input('Ingresa grados Celsius\n'))
        f=c*(9.0/5)+32
        print (str(c)+'ºC es igual a'+str(f)+'ºF')
    else:
        f=float(input('Ingresa grados Fahrenheit\n'))
        c=(f-32)*(5.0/9)
        print (str(f)+'ºF equivale a '+str(c)+'ºC ')
        
print Conversion()
