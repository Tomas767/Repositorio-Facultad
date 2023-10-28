import os

iteraciones = 0

flag_bmc = True

flag_imu = True

acomulador_jab = 0

while iteraciones != 5:
    
    while True:
        tipo_compra = input("barbijo\njabon\nalchol\nObjeto comprado? ")
        
        match tipo_compra:
            case "barbijo":
                break
            case "alchol":
                break
            case "jabon":
                break
            case other:
                print("informacion erronea/ objeto no valido")

    
    while True:
        precio = input("ingrese el precio del producto: ")

        if precio.isnumeric():
            precio = int(precio)

            if precio >= 100 and precio <= 300:
                break
            
            else:
                print("precio fuera de los limites")
        else:
            print("precio no valido")

    while True:
        unidades = input("ingrese la cantidad de unidades: ")

        if unidades.isnumeric():
            unidades = int(unidades)

            if unidades > 0 and unidades < 1000:
                break

            else:
                print("unidades fuera de los limites")

        else:
            print("la cantidad de unidades establecida no es valida")
    
    while True:
        fabricante = input("ingrese el nombre del fabricante: ")
        
        if fabricante != "":
            break
        
        else:
            print("no ingreso nada")

    if flag_bmc:
        precio_bmc = precio

        unidades_bmc = unidades

        fabricante_bmc = fabricante

        flag_bmc = False

    else:
        if precio > precio_bmc:
            precio_bmc = precio

            unidades_bmc = unidades

            fabricante_bmc = fabricante

    if flag_imu:
        unidades_imu = unidades

        fabricante_imu = fabricante

        flag_imu = False

    else:
        if unidades > unidades_imu:
            unidades_imu = unidades

            fabricante_imu = fabricante
    
    if tipo_compra == "jabon":
        acomulador_jab += unidades

    iteraciones += 1

print(f"""el fabricante y unidades del barbijo mas caro son:
fabricante: {fabricante_bmc}
unidades: {unidades_bmc}""")
print(f"""el fabricante del objeto con mas unidades es {fabricante_imu}""")
print(f"la cantidad total de jabones es de {acomulador_jab}")