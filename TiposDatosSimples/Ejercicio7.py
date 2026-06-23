#Ejercicio 7
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable,
#y muestre por pantalla la frase: Tu índice de masa corporal es <imc> 
#donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

#El Índice de Masa Corporal (IMC) se calcula dividiendo el peso de una persona (en kilogramos) 
#entre el cuadrado de su altura (en metros). 
#La fórmula es:\(IMC = \frac{\text{Peso (kg)}}{\text{Altura (m)}^2}\)

weigh = input("Ingresa tu peso: ")
heigh = input("Ingresa tu altura: ")

weigh = float(weigh)
heigh = float(heigh)

print (f"Tu peso es {weigh} kilogramos")

print (f"Tu altura es {heigh} centimetros")

imc = weigh / heigh**2
imc = round(imc,6)

print (f"Tu indice de masa corporal es {imc}")