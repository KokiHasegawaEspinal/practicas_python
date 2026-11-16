#Ejercicio 11
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
#una a una las letras de la palabra introducida empezando por la última.

usuario_palabra = input("Ingresa una palabra: ")

#for i in range(10, 0, -1):
#    print (i)
    

#print(usuario_palabra[::-1])

for i in range(len(usuario_palabra)-1, -1, -1):
    print(usuario_palabra[i])
