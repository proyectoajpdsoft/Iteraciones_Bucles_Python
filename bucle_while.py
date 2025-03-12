i = 0
print("Inicio del bucle while")
while i <= 2:
    print(f"Iterando en {i}")
    i += 1
print("Fin del bucle while")

i = 2
j = 0
print("Inicio del bucle while")
while i <= 260:
    j += 1
    print(f"El valor de la variable de control en la iteración {j}: {i}")
    i = i * i
print("Fin del bucle while")

i = 0
print("Inicio del bucle while")
while i > 0:
    print(f"Iterando en {i}")
    i += 1
print("Fin del bucle while")

numeroEntrada = int(input("Introduzca un número: "))
print("Inicio del bucle while")
while numeroEntrada <= 0:
    print("Ha introducido un número negativo o cero, por favor, introduzca un número mayor que cero")
    numeroEntrada = int(input("Introduzca un número: "))
print(f"Fin del bucle while")
print("Continuamos con otro bucle for, con número de repeticiones mayor que cero")
for i in range(numeroEntrada):
  print(f"Iteramos con bucle for, iteración {i}")
print(f"Fin del bucle for")