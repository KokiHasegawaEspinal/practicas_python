#Ejercicio 7
#Los tramos impositivos para la declaración de la
#renta en un determinado país son los siguientes:

#|          Renta          |  Tipo impositivo  |
#|-------------------------|-------------------|
#|     Menos de 10000€     |        5%         |
#|  Entre 10000€ y 20000€  |       15%         |
#|  Entre 20000€ y 35000€  |       20%         |
#|  Entre 35000€ y 60000€  |       30%         |
#|      Más de 60000€      |       45%         |

#Escribir un programa que pregunte al usuario su renta anual
#y muestre por pantalla el tipo impositivo que le corresponde.

tipo_impositivo = {
    "A":5,
    "B":15,
    "C":20,
    "D":30,
    "E":45
}

renta_usuario =int(input("Ingresa tu renta anual: "))

if renta_usuario < 10000:
    tramo = "A"
elif renta_usuario < 20000:
    tramo = "B"
elif renta_usuario < 35000:
    tramo = "C"
elif renta_usuario < 60000:
    tramo = "D"
else:
    tramo = "E"
    
print (f"Le corresponde {tipo_impositivo[tramo]}% de tipo impositivo")