# Ingresar el numero x que va a ser elevado a la n
n = int(input("Ingrese un número natural: ")) 
x = int(input("Ingrese un número real: "))
po = 1 
for i in range(1,x+1): # Se va a repetir las veces que se quiera multuplicar el número x por n
    po = po*n # Se multiplica por si mismo y po va guardando el resultado

print(str(n)+" ^ "+ str(x)+" = "+str(po))