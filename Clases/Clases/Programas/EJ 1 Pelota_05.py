# -*- coding: utf-8 -*-
# Cardoso Tovar Edwin
print 34*3 - 1.0/2*9.81*3**2
print 34*1 - 1.0/2*9.81*1**2 #acción
print 34*1.5 - 1.0/2*9.81*1.5**2
print 34*5 - 1.0/2*9.81*5**2
v0 = 34
g = 9.81
t = 4.3
y = v0*t - 1.0/2*g*t**2
print y
print 'La posición de la pelota en el t=%30g es %20.2E\n%f' % (t,y,t) # %g es una cadena de control en python, no tiene nada que ver con g de gravedad
#y es el primer valor la cual es la variable t y la otra es del valor final (%.4f) por eso se pone %(t,y)

