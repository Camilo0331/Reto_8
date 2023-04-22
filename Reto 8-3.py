i : int
i = int(input("Ingrese un número entero: ")) #Se pide que ingrese un número
if i % 2 != 0: #Sí modulado 2 es distinto a 0, restar uno para que sea par
   i = i - 1
for u in range(i, 1, -2): #Se genera el rango y se va restando de a dos para que vaya dando pares
    print(u)# Se imprime la lista