def vAbsoluto(x):
    if x >=0:
        return(x)
    else:
        return(-x)

def raiz(x):
    h=x
    b=1.0
    e=0.0001
    while vAbsoluto(b-h)>e:
        h= (b+h)/2
        b= x/h
    return(b)

def raiz1(x):
    h=x
    b=1.0
    e=0.0001
    while vAbsoluto(b-h)>e:
        h= (b+h)/2
        b= x/h
    return(b)












