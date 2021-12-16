def funcionFactorial(numero):
    if numero==1 or numero==0:
        return 1
    else:
        return numero*funcionFactorial(numero-1)
    
def MCD(numero1,numero2):
    q = numero1/numero2
    r = numero1%numero2
    
    if r==0:
        return numero2
    else:
        return MCD(numero2,r)

def MCM(numero1,numero2):
    mcd = MCD(numero1,numero2)
    mcm = numero1*numero2/mcd
    
    return mcm

#Serie de Fibonacci

def termino_fibonacci(numero): #5   
    if numero==1:
        return 0
    elif numero==2:
        return 1
    else:
        #return termino_fibonacci(numero-1) #4,3        
        lista_terminos = [0,1]
        #Agrega hasta que termino
        for x in range(numero-2): #0,1,2
            termino = lista_terminos[x] + lista_terminos[x+1] #1 |2 | 3
            #print(termino)
            lista_terminos.append(termino) #[0,1,1] | [0,1,1,2] | [0,1,1,2,3]
            #print(lista_terminos)
        
        return lista_terminos
    

def suma_fibonacci(numero):
    suma=0
    lista_terminos = termino_fibonacci(numero)
    if isinstance(lista_terminos,int):
        if lista_terminos==0:
            suma=0            
        else:
            suma=1
    else:
        for element in lista_terminos:
            suma+=element
    
    return suma

resultado = suma_fibonacci(2)
print(resultado)