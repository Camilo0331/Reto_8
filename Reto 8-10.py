import math #Importe math para las operaciones

def exponente(x:int): #Se define la función para exponentes
    return math.exp(x)

def seriemc(x:int, i:int): #Se define la función maclaurin
    mc = 0
    for b in (0, i +1):
        mc = (-1**i)*((x**(2*i+1))/(2*i+1)) #Se pone la ecuación que se solicita
        return mc
    
if __name__ == "__main__":
    #Se pide los números
    x = int(input("Ingrese un número x: "))
    i = int(input("Ingrese la cantidad de Maclaurin: "))
    exponen = exponente(x) #Se llama la función exponente
    print(exponen)
    maclaurin = seriemc(x, i) #Se llama la función seriemc
    print(maclaurin)