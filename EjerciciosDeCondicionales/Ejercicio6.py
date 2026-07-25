#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A
#y B de acuerdo al sexo y el nombre. El grupo A esta formado
#por las mujeres con un nombre anterior a la M y los hombres
# con un nombre posterior a la N y el grupo B por el resto.
#Escribir un programa que pregunte al usuario su nombre y sexo,
#y muestre por pantalla el grupo que le corresponde.

grupo = {
    "A": "grupo A",
    "B": "grupo B"
}   

nombre = input("Ingresa tu nombre: ").upper()
sexo = input("Ingresa tu genero (M/F):").upper()

if sexo == "F":
    if nombre[0] < "M":
        grupo_print=grupo['A']
    elif nombre[0] >= "M":
        grupo_print=grupo['B']        
else:
    if nombre[0] > "N":
        grupo_print=grupo['A']
    elif nombre[0] <= "N":
        grupo_print=grupo['B']

print(f"{nombre.title()} pertenece al {grupo_print}")

    
    
    
    
    
    