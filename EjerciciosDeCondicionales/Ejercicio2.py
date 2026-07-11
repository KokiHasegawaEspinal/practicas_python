#Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres contraseña
#en una variable, pregunte al usuario por la contraseña e imprima por
#pantalla si la contraseña introducida por el usuario coincide con la
#guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password_saved = "asjeu12asdkjh87"

password_introducida = input("Ingresa tu contraseña: ")


if password_introducida.lower() == password_saved.lower():
    print(f"La contraseña introducida es correcta, lograste autenticarte")
else:
    print(f"la contraseña introdocida es incorrecta, intenta de nuevo!")
