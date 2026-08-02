#Ejercicio 10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus
#clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana
#o no, y en función de su respuesta le muestre un menú con los ingredientes
#disponibles para que elija. Solo se puede eligir un ingrediente además de la
# mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar
# por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print(" Bienvenido a La pizzería Bella Napoli")

pizza_usuario = input("Desea una pizza vegetariana? ").upper()

ingredientes_comunes = {
    "MOZZARELLA":"mozarella",
    "TOMATE":"tomate"
}

ingredientes_vegetarianos = {
    "PIMIENTO":"pimiento",
    "TOFU":"tofu"
}

ingredientes_no_vegetarinos = {
    "PEPERONI":"peperoni",
    "JAMON":"jamón",
    "SALMON":"salmón"
}

print(f"Los ingredientes base de las pizzas son: {ingredientes_comunes['MOZZARELLA']} y {ingredientes_comunes['TOMATE']}")

if pizza_usuario == "SI":
    pizza_tipo = "Pizza vegetariana"
    ingredientes_usuario = input(f"Escoja un topping ({ingredientes_vegetarianos['PIMIENTO']} o {ingredientes_vegetarianos['TOFU']}): ").upper()
else:
    pizza_tipo = "Pizza no vegetariana"
    ingredientes_usuario = input(f"Escoja un topping ({ingredientes_no_vegetarinos['PEPERONI']} o {ingredientes_no_vegetarinos['JAMON']} o {ingredientes_no_vegetarinos['SALMON']}): ").upper()
    
print (f"La pizza que ordenó es {pizza_tipo}")
print (f"Los ingredientes que contiene la {pizza_tipo} son: ")
print (f"Ingredientes comunes: {ingredientes_comunes['MOZZARELLA']} y {ingredientes_comunes['TOMATE']}")

if pizza_tipo == "Pizza vegetariana":
    print (f"El topping que elegio es {ingredientes_vegetarianos[ingredientes_usuario]}")
else:
    print (f"El topping que eleigio es {ingredientes_no_vegetarinos[ingredientes_usuario]}")

print ("Muchas gracias por su preferencia")

