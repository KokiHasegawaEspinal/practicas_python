#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres
##contraseña en una variable, pregunte al usuario por la
#contraseña hasta que introduzca la contraseña correcta.

contrasena = "jasKLj!kd12"


while True:
#    usuario_contrasena = input("Ingresa tu contraseña: ").upper()
#    if usuario_contrasena == contrasena.upper():
    usuario_contrasena = input("Ingresa tu contraseña: ")
    if usuario_contrasena == contrasena:
        print ("Contraseña correcta")
        break
    else:
        print ("Contraseña incorrecta, vuelve a intentar!")