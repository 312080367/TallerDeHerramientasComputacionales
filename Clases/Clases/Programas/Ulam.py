def paridad(x):
#    if x/2 == d and 2*d == x :
#        return(si)
#    else:
#        return(no)

        
#def sucULAM(x):
# a = x/2
#    b = 3*x+1
#    while :
#       if paridad(si):
#            print(a)
#        else :
#            print(b)

def ulam(x):
    #if (x/2)*2-x== 0:(tambien se puede usar esto)
    if x%2==0: #este % es el modulo que nos ayuda a ver si una division es intera o no,si da entero se va a x/2, si no es asi se va a 3*x+1
    
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
