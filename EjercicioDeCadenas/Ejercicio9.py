#Ejercicio 9
#Escribir un programa que pregunte al usuario la fecha de su
#nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día,
#el mes y el año. Adaptar el programa anterior para que también
#funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha_nacimiento = input("Escribe la fecha de tu nacimiento (Formato a usar dd/mm/aaaa: ")

primer_slash = fecha_nacimiento.find("/")
dia_nacimiento = fecha_nacimiento[:primer_slash]
print(f"El dia de nacimiento es: {dia_nacimiento}")

segundo_slash = fecha_nacimiento.find("/", primer_slash+1)
#primer_slash(segundo_slash)
mes_nacimiento = fecha_nacimiento[primer_slash+1:segundo_slash]
print(f"El mes de nacimiento es: {mes_nacimiento}")

año_nacimiento = fecha_nacimiento[segundo_slash+1:]
print(f"El añ0 de nacimiento es: {año_nacimiento}")

