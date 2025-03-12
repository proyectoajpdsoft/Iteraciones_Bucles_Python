print("Iniciamos un bucle for con una lista de números")
for i in [1, 2, 5, 12,10, 3]:
    print(f"Iterando en elemento {i}")
print("Finalizó el bucle for")

print("Iniciamos un bucle for con una lista de cadenas de texto")
for i in ["España", "Francia", "Portugal", "Italia", "Alemania"]:
    print(f"Iterando en elemento {i}")
print("Finalizó el bucle for")

print("Iniciamos un bucle for con un texto y su iteración por cada carácter")
for i in "Por carácter":
    print(f"Iterando en elemento {i}")
print("Finalizó el bucle for")

print("Iniciamos un bucle for con range")
for i in range(4):
    print(f"Iterando en elemento {i}")
print("Finalizó el bucle for")  

numVeces = int(input("¿Cuántas veces quiere que sume 4 + 9? "))
print("Iniciamos un bucle for con range y valor pedido por consola")
for i in range(numVeces):
    print(f"La suma de 4 + 9 es: {4+9}")
print("Finalizó el bucle for")

print("Iniciamos un bucle for con range y contamos las veces que se ejecuta")
contador = 0
for i in range(3):
    print(f"Iterando con {i}")
    contador += 1
print(f"Finalizó el bucle for, se ejecutó {contador} veces")

print("Iniciamos un bucle for con range y sumamos su iterador")
suma = 0
for i in range(4):
    print(f"Iterando con {i}")
    suma += i
print(f"Finalizó el bucle for, suma de sus iteradores: {suma}")

print("Iniciamos un bucle for con range, mínimo, máximo, intervalo")
for i in range(4, 8, 2):
    print(f"Iterando con {i}")
print("Finalizó el bucle for")

print("Iniciamos un bucle for con range, sin elemento actual (i)")
for _ in range(1, 3):
    print(f"Iterando sin elemento actual")
print("Finalizó el bucle for")

print("Iniciamos un bucle for con range, mínimo, máximo, intervalo y break para forzar salida")
for i in range(2, 8, 1):
    if i > 5:
        print(f"Se forzó la finalización del bucle for con break")
        break        
    print(f"Iterando con {i}")
print("Finalizó el bucle for")

print("Iniciamos un bucle for con una lista para mostrar sólo los números pares")
numeros = [1, 2, 5, 8, 3, 0, 28, 11]
for i in numeros:
    if i % 2 != 0:
        continue
    print("{0} es par".format(i))
print("Finalizó el bucle for")

print("Iniciamos un bucle for..else con range, mínimo, máximo, intervalo y break para forzar salida y que continúe por el else")
for i in range(2, 8, 1):
    if i > 5:
        print(f"Se forzó la finalización del bucle for con break")
        break        
    print(f"Iterando con {i}")
else:
    print("Se salió del bucle anterior con break")
print("Finalizó el bucle for..else")

print("Iniciamos un bucle for recorriendo un diccionario y mostrando su índice")
paises = {"España": 34, "Francia": 33, "Italia": 39, "Portugal": 351, 
          "Alemania": 49, "Andorra": 376, "Bélgica": 32}
for i in paises:
    print(i)
print("Finalizó el bucle for")

print("Iniciamos un bucle for recorriendo un diccionario y mostrando sus valores")
paises = {"España": 34, "Francia": 33, "Italia": 39, "Portugal": 351, 
          "Alemania": 49, "Andorra": 376, "Bélgica": 32}
for i in paises.values():
    print(i)
print("Finalizó el bucle for")

colores = ["Verde", "Azul", "Rojo", "Amarillo", "Naranja", "Marrón", "Negro"]
print("Inicio del bucle for recorriendo elementos de lista")
for color in colores:
    print (color)
print("Fin del bucle for")

colores = ["Verde", "Azul", "Rojo", "Amarillo", "Naranja", "Marrón", "Negro"]
print("Inicio del bucle for recorriendo elementos de lista con range")
for i in range(0, len(colores)):
    print (colores[i])
print("Fin del bucle for")