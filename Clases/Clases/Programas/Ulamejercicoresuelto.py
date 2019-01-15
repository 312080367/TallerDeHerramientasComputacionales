def ulam(x):
    #if (x/2)*2-x== 0:(tambien se puede usar esto)
    if x%2==0:
    
        return x/2
    else:
        return 3*x+1
#el problema lo dividimos en partes para ir solucionando eficazmente
    
def suc(x):
    i=0
    #while x>1:(tambien asi se puede)
    while x!=1:
        x=ulam(x)
        i=i+1
    return i    
        
print ulam(52)

print suc(7)
print suc(26)
print suc(52)
print suc(1024)
print suc(72)
print suc(1524927)
print suc(2)
#al final ponemos los dos print para los resultados de las dos funciones

#Siempre es mejor dividir el problema en dos partes, por ejemplo 
