from data import *
import os

while True:
    while True:
        op = input("""
                    MENU
--------------------------------------------
favor de escribir unicamente 
el numero para seleccionar
la opcion
--------------------------------------------
1: recorrer la lista de superheroes
                   
2: mostrar identidad y peso del superheroe mas fuerte
                   
3: mostrar nombre e identidad del superheroe mas bajo(altura)
                   
4: mostrar promedio de la altura de los superheroes masculinos
                   
5: Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino

opcion deseada: """)
        
        match(op):
            case "1":
                break
            
            case "2":
                break

            case "3":
                break

            case "4":
                break

            case "5":
                break

            case other:
                print("descripcion no valida")

                os.system("pause")

                os.system("cls")
        
        break

    match(op):
        case "1":
            for dato in lista_personajes:
                for clave, valor in dato.items():#items() devuelve una tupla de tanto la clave
                    print(f"{clave}: {valor}")     # como su valor para utilizarlo de manera conveniente
                print("-------------------------------------------")

        case "2":

            flag_max = True

            identidades = []

            pesos = []

            for dato in lista_personajes:
                for clave, valor in dato.items():
                    x = dato["identidad"]
                    

                    x2 = dato["peso"]

                    if clave == "fuerza":
                        valor = float(valor)

                        if flag_max:
                            min = valor

                            a = x

                            identidades.append(x)

                            b = x2  

                            pesos.append(x2)
                            
                            flag_max = False

                        elif valor > min:
                            min = valor

                            index = identidades.index(a)

                            a = x

                            identidades[index] = x

                            index2 = pesos.index(b)

                            b = x2

                            pesos[index2] = x2

            for dato in lista_personajes:
                for clave2, valor2 in dato.items():
                    y = dato["identidad"]

                    y2 = dato["peso"]

                    if clave2 == "fuerza":
                        valor2 = float(valor2)

                        for element in identidades:
                            if y != element:
                                if valor2 == min:
                                    identidades.append(y)

                                    pesos.append(y2)

            print(f"la identidad y el peso del superheroe/s mas fuerte es de:")

            for x in range(len(identidades)):
                print(f"\nidentidad: {identidades[x]}")
                print(f"peso: {pesos[x]}\n--------------------------")
                

        case "3":

            flag_max = True

            identidades = []

            nombres = []

            for dato in lista_personajes:
                for clave, valor in dato.items():
                    x = dato["identidad"]
                    

                    x2 = dato["nombre"]

                    if clave == "altura":
                        valor = float(valor)

                        if flag_max:
                            maximo = valor

                            a = x

                            identidades.append(x)

                            b = x2  

                            nombres.append(x2)
                            
                            flag_max = False

                        elif valor < maximo:
                            maximo = valor

                            index = identidades.index(a)

                            a = x

                            identidades[index] = x

                            index2 = nombres.index(b)

                            b = x2

                            nombres[index2] = x2

            for dato in lista_personajes:
                for clave2, valor2 in dato.items():
                    y = dato["identidad"]

                    y2 = dato["peso"]

                    if clave2 == "altura":
                        valor2 = float(valor2)

                        for element in identidades:
                            if y != element:
                                if valor2 == maximo:
                                    identidades.append(y)

                                    nombres.append(y2)

            print(f"el nombre y la identidad del superheroe/s mas pequeño es de:")

            for x in range(len(identidades)):
                print(f"\nnombre: {nombres[x]}")
                print(f"identidad: {identidades[x]}\n--------------------------")

        case "4":
            count = 0    

            accomulator = 0
            
            for data in lista_personajes:
                count += 1

                for clave, valor in data.items():
                    if valor == "M":
                        valor = float(data["peso"])
                        
                        accomulator += valor
            
            if count != 0 and accomulator != 0:
                promedio = accomulator / count

            else:
                promedio = "no se produjo ningun promedio"

            print(f"el promedio de peso de los superheroes masculinos es: {promedio}")

        case "5":
            count = 0    

            accomulator = 0
            
            for data in lista_personajes:
                count += 1

                for clave, valor in data.items():
                    if valor == "F":
                        valor = float(data["fuerza"])
                        
                        accomulator += valor
            
            if count != 0 and accomulator != 0:
                promedio = accomulator / count

            else:
                promedio = "no se produjo ningun promedio"

            nombres = []

            pesos = []

            for personje in lista_personajes:
                for clave, valor in personje.items():
                    if clave == "fuerza":
                        y = float(valor)

                        if y > promedio:
                            nombres.append(personje["nombre"])

                            pesos.append(personje["peso"])

            print(f"""
los superheroes mas fuertes, al promedio de la fuerza de los supers
femeninos, y su nombre y peso son:
""")
            for x in range(len(nombres)):
                print(f"nombre: {nombres[x]}\npeso: {pesos[x]}\n-------------------------")
    
    os.system("pause")

    os.system("cls")
