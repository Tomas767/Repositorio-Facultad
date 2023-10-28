import os

amigos = []
comidas = []
total_comidas = []
bebidas = []
total_bebidas = []

acomulador_bebidas = 0
acomulador_comidas = 0

acomulador_jugo = 0

contador_p = 0
contador_e = 0
contador_h = 0

flag = True

continuar = "s"

PRECIO_COMIDA = 800
PRECIO_BEBIDA = 200

while True:
    promedio_p = 0
    promedio_e = 0
    promedio_h = 0

    nombre = input("Ingrese su nombre: ")

    while nombre == None and not nombre.isalpha():

        nombre = input("Ingrese su nombre nuevamente: ")
    
    amigos.append(nombre)
    

    while True:
        comida = input("""comida disponible:
Pizza
Hamburguesa
Ensalada
Seleccionado: """).capitalize()

        match(comida):
            case "Pizza":
                break
            case "Hamburguesa":
                break
            case "Ensalada":
                break
            case other:
                print("comida seleccionada no valida, ingrese nuevamente")
                os.system("pause")

    comidas.append(comida)

    while True:
        cantidad_comidas = input("ingrese la cantidad comidas de pedidas: ")

        if cantidad_comidas.isnumeric() and int(cantidad_comidas) > 0:

            cantidad_comidas = int(cantidad_comidas)

            break
        else:

            print("Error, ingrese nuevamente el dato")
    
    match(comida):
        case "Pizza":
            contador_p += cantidad_comidas
        case "Hamburguesa":
            contador_h += cantidad_comidas
        case "Ensalada":
            contador_e += cantidad_comidas

    total_comidas.append(cantidad_comidas)

    while True:
        bebida = input("""bebida disponible:
Refresco
Agua
Jugo
Seleccionado: """).capitalize()
        
        match(bebida):
            case "Refresco":
                break
            case "Agua":
                break
            case "Jugo":
                break
            case other:
                print("bebida seleccionada no valida, ingrese nuevamente")
                os.system("pause")

    bebidas.append(bebida)

    while True:
        cantidad_bebidas = input("ingrese la cantidad de bebidas pedidas: ")

        if cantidad_bebidas.isnumeric() and int(cantidad_bebidas) > 0:
            cantidad_bebidas = int(cantidad_bebidas)
            break
        else:
            print("Error, ingrese nuevamente el dato")

    total_bebidas.append(cantidad_bebidas)

    continuar = input("""agregar otro amigo
's' para continuar
Enter para finalizar""")
        
    if continuar == "":
        break

cantidad_amigos = len(amigos)

for x in range(len(bebidas)):

    cantidad = total_bebidas[x]

    if bebidas[x] == "Jugo":

        acomulador_jugo = acomulador_jugo + cantidad

if contador_p != 0:
    promedio_p = (contador_p * 100) / cantidad_amigos

if contador_h != 0:
    promedio_h = (contador_h * 100) / cantidad_amigos

if contador_e != 0:
    promedio_e = (contador_e * 100) / cantidad_amigos

for nombre in range(len(amigos)):

    cont_c = total_comidas[nombre]

    cont_b = total_bebidas[nombre]
    
    total_pedidos = cont_c + cont_b

    if flag:
        ganador = amigos[nombre]
        pedidos = total_pedidos
    else:
        if total_pedidos > pedidos:
            ganador = amigos[nombre]
            pedidos = total_pedidos

for x in total_comidas:

    acomulador_comidas = acomulador_comidas + x

for x in total_bebidas:

    acomulador_bebidas = acomulador_bebidas + x


total_gastado = (acomulador_comidas * PRECIO_COMIDA) + (acomulador_bebidas * PRECIO_BEBIDA)

if acomulador_jugo != 0:
    total_jugo = acomulador_jugo * PRECIO_BEBIDA

    promedio_jugo = total_jugo / cantidad_amigos

propina = (10 * total_gastado) / 100

gasto_final = propina + total_gastado

print(f"el total de la cuenta es {total_gastado} mas propina del 10% al mesero seria {gasto_final}")

if promedio_jugo != None:
    print(f"el promedio gastado en jugo es {promedio_jugo}")
else:
    print("no se compro jugo")

print(f"""el promedio de los platos pedidos son
Pizza {promedio_p}%
Hamburguesa {promedio_h}%
Ensalada {promedio_e}%""")

print(f"el ganador, que realizo mas pedidos en total es {ganador}\nhabiendo pedido {pedidos}")


