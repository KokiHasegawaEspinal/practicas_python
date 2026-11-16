#Ejercicio 12
#Escribir un programa en el que se pregunte al usuario
#por una frase y una letra, y muestre por pantalla el
#número de veces que aparece la letra en la frase.

frase_usuario = input("Escribe una frase: ")
letra_usuario = input("Escribe una letra: ")

count = 0
for letra in frase_usuario:
    if letra == letra_usuario:
        count = count +1
print(count)