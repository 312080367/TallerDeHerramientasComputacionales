#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'Dada una pareja de números calcular el m.c.d'
def mcd(x,y):
    resto = 0
    while(b>0):
        resto = b
        b = a%b
        a = resto
    return a
 
int(input('Introduzca 2 números enteros positivos después de 1'))

num1= int(input('escriba el primer número'))
num2= int(input('escriba el segundo numero'))

print("El máximo común divisor de",num1,"y",num2,"es", mcd(num1,num2))
