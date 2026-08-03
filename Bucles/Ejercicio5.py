#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años, y muestre por pantalla el
#capital obtenido en la inversión cada año que dura la inversión.

cantidad_invertir = int(input("Ingrese la cantidad que desea invertir: "))

interes_anual = float(input("Ingrese la tasa de interes anual: "))/100

numero_anos = int(input("Ingrese la cantidad de años que desea invertir: "))

for i in range(1, numero_anos + 1):
    capital_obtenido = cantidad_invertir*(1 + interes_anual)
    print (f"Año {i}: {capital_obtenido:.2f} €")
    cantidad_invertir = capital_obtenido