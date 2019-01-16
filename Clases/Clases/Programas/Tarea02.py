# -*- coding: utf-8 -*-
# Un automóvil mantiene una aceleración constante de 8 m/s². Si su velocidad inicial era de 20 m/s al norte, ¿cuál será su velocidad después de 6s?
print 20 + 8*2
print 20 + 8*4
print 20 + 8*7
print 20 + 8*3.5

ac= 8
v0= 20
t=6
y= v0 + ac*t
print y
print 'la velocidad final en el t=%30g es 2%20.2E\n%f' %(t,y,ac)


def velocidadfinal(t,v0,ac):
    y= v0* + ac*t
    return(y)
