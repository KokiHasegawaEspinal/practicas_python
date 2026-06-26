#Ejercicio 9
#Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

#La fórmula matemática general para calcular el capital final es:(CF = CI (1 + i)^n
#Donde:CF = Capital Final (el dinero total que tendrás al final de la inversión).
#CI = Capital Inicial (el dinero que inviertes al principio).i = Tasa de interés por periodo,
#expresada en decimal (por ejemplo, 8% se escribe como 0,08).n = Número de periodos 
#(meses, años, etc., dependiendo de cómo se aplique el interés).

CI = int(input("Qué cantidad quisieras invertir: "))

i = float(input("Escoge una tasa anual (En decimales): "))

n = int(input("Cuanto tiempo, en años, deseas invertir: "))

CF = CI*(1+i)**n

i = int(i*100)

CF = round(CF,2)

print (f"El capital obtenido en la inversion de ${CI} por {n} años, a una tasa anual de {i}% es: $ {CF}")