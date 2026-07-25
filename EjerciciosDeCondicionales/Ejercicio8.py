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
    puntuacion = 0.0
elif puntuacion_usuario == 0.4:
    rendimiento = "Aceptable"
    puntuacion = 0.4
elif puntuacion_usuario >= 0.6:
    rendimiento = "Meritorio"
    puntuacion = puntuacion_usuario
else:
    print ("Valor ingresado no correcto, vuelva a intentar")
    
dinero_conseguido = dinero_multiplicador * puntuacion

print (f"Tu rendimiento es {rendimiento} y la cantidad de dinero a recibir por dicho rendimiento es de {dinero_conseguido}€")