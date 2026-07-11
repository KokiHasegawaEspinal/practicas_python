#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor
#de 16 años y tener unos ingresos iguales o superiores a
#1000 € mensuales. Escribir un programa que pregunte al
#usuario su edad y sus ingresos mensuales y muestre
#por pantalla si el usuario tiene que tributar o no.

edad_minima = 16

ingreso_minimo = 1000

preguntar_edad = int(input("Cuá es tu edad? "))
preguntar_ingresos_mesuales = int(input("Cuál es tu ingreso mensual? "))

if preguntar_edad > edad_minima and preguntar_ingresos_mesuales >= ingreso_minimo:
    print("Usted cumple con los requisitos para tributar")
    print(f"Usted tiene que tributar!")
    
else:
    print("Usted no cumple con los requisitos para tributar!")
    print(f"Debes cumplir con los siguientes requisitos:")
    print(f"Ser mayor de {edad_minima} años y tener ingresos mensuales igual o superori a {ingreso_minimo}")
