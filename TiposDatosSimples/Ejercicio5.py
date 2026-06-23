#Ejercicio 5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas 
#y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = input ("Cuantas horas has trabajado: ")

costo_hora = input ("Cual es el costo por hora: ")

pago = int(horas_trabajadas) * int(costo_hora)

print (f"Te corresponde S/{pago} por {horas_trabajadas} horas trabajadas a un costo de {costo_hora} soles por hora")