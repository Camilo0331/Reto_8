def potencia(i:int): #Se define la función 
    n = 1
    for i in range(1, i +1): #Se define el rango
        n = n*2 # n será la que vaya guardando los resultados 
    return n
    
if __name__ == "__main__":
    po = int(input("Ingrese el número de veces que potencia a 2: ")) # Ingrese el número
    poten = potencia(po) # Se llama la función
    print(poten) #Se imprime la potencia