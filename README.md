# Reto_8
El city va a ganar la champions

## Punto 1

Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```
for i in range(1,101): # el rango va de 1 a 100
    print("El cuadrado del número "+ str(i)+" es: "+ str(i**2)) # para cada número va a sar su cuadrado
```

## Punto 2

Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```
print("Lista de números impares hasta el 999") 
for i in range(1,1000, 2): # Se genera el rango de los numero a tomar,cada 2 en 2
    print(i) # se imprimen los números impares

if __name__ == "__main__":
    print("Lista de números pares hasta 1000") 
    for u in range(2,1001,2):  # Se genera el rango de los numero a tomar,cada 2 en 2
        print(u) # se imprimen los números pares
```

## Punto 3

Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```
i : int
i = int(input("Ingrese un número entero: ")) #Se pide que ingrese un número
if i % 2 != 0: #Sí modulado 2 es distinto a 0, restar uno para que sea par
   i = i - 1
for u in range(i, 1, -2): #Se genera el rango y se va restando de a dos para que vaya dando pares
    print(u)# Se imprime la lista
```

## Punto 4

Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

```
n = int(input("Ingrese un número: ")) # Ingresa el número
n +=1  # Se suma uno para que tome todos los números ingresados
for u in range(1,n): #Se genera el rango
   i = 1 
   while u > 0: #Mientras u sea menor a cero que vya haciendo los factoriales
      i = i * u # i guarda los resultados de nuestras multiplicaciones hasta que el while no cumpla la condición
      u -=1 # Se resta 1
   print ("El factorial "+ str(u)+" de ingresado es: "+str(i)) #Se imprime el número ingresado con su factorial
```

## Punto 5

Calcular el valor de 2 elevado a la potencia n usando ciclos for.

```
def potencia(i:int): #Se define la función 
    n = 1
    for i in range(1, i +1): #Se define el rango
        n = n*2 # n será la que vaya guardando los resultados 
    return n
    
if __name__ == "__main__":
    po = int(input("Ingrese el número de veces que potencia a 2: ")) # Ingrese el número
    poten = potencia(po) # Se llama la función
    print(poten) #Se imprime la potencia
```

## Punto 6

Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

```
# Ingresar el numero x que va a ser elevado a la n
n = int(input("Ingrese un número natural: ")) 
x = int(input("Ingrese un número real: "))
po = 1 
for i in range(1,x+1): # Se va a repetir las veces que se quiera multuplicar el número x por n
    po = po*n # Se multiplica por si mismo y po va guardando el resultado

print(str(n)+" ^ "+ str(x)+" = "+str(po))
```

## Punto 7

Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

```
for i in range(1,10): #Hice un for para tomar los números del 1 al 10
    for n in range(1, 10): #Este for es para que multuplique del 1 al 10 por el número que valga i
        multi = i * n
        print(str(i)+" * "+str(n)+" = "+str(multi))
```

## Punto 8

Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

![image](https://user-images.githubusercontent.com/124615019/233754891-96c3ce7b-9953-454f-a236-ece6ba7a9a10.png)

```
import math #Importe math para las operaciones

def exponente(x:int): #Se define la función para exponentes
    return math.exp(x)

def factorial(i: int): #Se define la función para los factoriales
    n = 1
    for f in (1, i):
        n *=f # n va a ir guardando las multiplicaciones que va tomando f
        return n
def seriemc(x:int, i:int): #Se define la función maclaurin
    mc = 0
    for b in (0, i +1): 
        mc = (x**i)/factorial(i) #Se pone la ecuación que se solicita
        return mc 
    
if __name__ == "__main__":
    #Se pide los números
    x = int(input("Ingrese un número x: "))
    i = int(input("Ingrese la cantidad de Maclaurin: "))
    exponen = exponente(x) #Se llama la función exponente
    print(exponen)
    maclaurin = seriemc(x, i) #Se llama la función seriemc
    print(maclaurin)
```

## Punto 9

Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

![image](https://user-images.githubusercontent.com/124615019/233754923-b1c450b4-8b6b-4b12-91a0-a4a53d2a166c.png)


```
import math #Importe math para las operaciones

def exponente(x:int): #Se define la función para exponentes
    return math.exp(x)

def factorial(i: int): #Se define la función para los factoriales
    n = 1
    for f in (1, i+1):
        n *=f # n va a ir guardando las multiplicaciones que va tomando f
        return n
def seriemc(x:int, i:int): #Se define la función maclaurin
    mc = 0
    for b in (0, i +1):
        mc = (-1**i)*((x**(2*i+1))/factorial(2*i+1)) #Se pone la ecuación que se solicita
        return mc
    
if __name__ == "__main__":
    #Se pide los números
    x = int(input("Ingrese un número x: "))
    i = int(input("Ingrese la cantidad de Maclaurin: "))
    exponen = exponente(x) #Se llama la función exponente
    print(exponen)
    maclaurin = seriemc(x, i) #Se llama la función seriemc
    print(maclaurin)
```

## Punto 10

Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

![image](https://user-images.githubusercontent.com/124615019/233754966-63e1f4d5-c5ae-4c7d-8aab-49bb3047ad7f.png)

```
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
```

### ¡No olviden dejar su estrella!
