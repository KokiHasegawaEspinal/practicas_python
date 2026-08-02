#Ejercicio 8
#En una determinada empresa, sus empleados son evaluados al final de cada año.
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
#aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
#los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre
#las cifras mencionadas. A continuación se muestra una tabla con los niveles
#correspondientes a cada puntuación. La cantidad de dinero conseguida en cada
#nivel es de 2.400€ multiplicada por la puntuación del nivel.

#|   Nivel    |	Puntuación|
#|------------|-----------|
#|Inaceptable |    0.0    |
#| Aceptable  |    0.4    |
#| Meritorio  | 0.6 o más |

#Escribir un programa que lea la puntuación del usuario e indique su nivel
#de rendimiento, así como la cantidad de dinero que recibirá el usuario.

dinero_multiplicador = 2400

puntuacion_usuario = float(input("Ingresa tu puntuacion: "))

if puntuacion_usuario == 0.0:
    rendimiento = "Inaceptable"
    valido = True
elif puntuacion_usuario == 0.4:
    rendimiento = "Aceptable"
    valido = True
elif puntuacion_usuario >= 0.6:
    rendimiento = "Meritorio"
    valido = True
else:
    valido = False

if valido:
    dinero_conseguido = dinero_multiplicador * puntuacion_usuario
    print (f"Tu rendimiento es {rendimiento} y la cantidad de dinero a recibir por dicho rendimiento es de {dinero_conseguido}€")
else:
    print("Ingresa un monto válido")