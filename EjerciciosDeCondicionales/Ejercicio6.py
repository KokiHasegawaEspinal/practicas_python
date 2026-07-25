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

#print(nombre)
#print(sexo)
#print (nombre.title())

if sexo == "F" and nombre[0] < "M":
    grupo_print=grupo['A']
#    print(f"{nombre.title()} pertenece al {grupo['A']}")
elif sexo == "F" and nombre[0] >= "M":
    grupo_print=grupo['B']
#    print(f"{nombre.title()} pertenece al {grupo ['B']}")
elif sexo == "M" and nombre[0] >"N":
    grupo_print=grupo['A']
#    print(f"{nombre.title()} pertenece al {grupo ['A']}")
else:
    grupo_print=grupo['B']
#    print(f"{nombre.title()} pertenece al {grupo ['B']}")

print(f"{nombre.title()} pertenece al {grupo_print}")

    
    
    
    
    
    