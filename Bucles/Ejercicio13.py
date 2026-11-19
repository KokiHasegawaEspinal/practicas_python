#Ejercicio 13
#Escribir un programa que muestre el eco
#de todo lo que el usuario introduzca hasta
#que el usuario escriba “salir” que terminará.


fin_programa = "salir"
eco_usuario = input ("Introduce una palabra: ")

while True:
    if eco_usuario == fin_programa:
        print(f"eco: {eco_usuario}")
        print ("Gracias por participar, terminó el juego!")
        break
    else:
        print(f"eco: {eco_usuario}")
        eco_usuario = input ("Introduce una palabra: ")
    
