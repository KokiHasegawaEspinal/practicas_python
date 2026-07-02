#Ejercicio 7
#Escribir un programa que pregunte el correo electrónico del usuario
#en la consola y muestre por pantalla otro correo electrónico con el
#mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo_electronico = input("Escribe tu correo electronico: ")

buscar_arroba = correo_electronico.find("@")
print(buscar_arroba)

extraer_correo = correo_electronico[:buscar_arroba]
print(extraer_correo)

agregar_dominio = "ceu.es"

nuevo_correo = extraer_correo + "@" + agregar_dominio

print(nuevo_correo)