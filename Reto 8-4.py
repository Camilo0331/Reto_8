n = int(input("Ingrese un número: ")) # Ingresa el número
n +=1  # Se suma uno para que tome todos los números ingresados
for u in range(1,n): #Se genera el rango
   i = 1 
   while u > 0: #Mientras u sea menor a cero que vya haciendo los factoriales
      i = i * u # i guarda los resultados de nuestras multiplicaciones hasta que el while no cumpla la condición
      u -=1 # Se resta 1
   print ("El factorial "+ str(u)+" de ingresado es: "+str(i)) #Se imprime el número ingresado con su factorial