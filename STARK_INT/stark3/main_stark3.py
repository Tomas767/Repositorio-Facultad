from funciones_main_stark3 import *

from data import lista_personajes

import os

bandera_1 = False

while True:

    os.system("cls")

    op = stark_menu_principal()

    match(op):
        case "1":
            if not bandera_1:
                datos, bandera_1 = stark_normalizar_datos(lista_personajes)
            
            else:
                print("los datos ya fueron normalizados")

        case "2":   
            if bandera_1:
                for dato in datos:
                    bandera_2 = obtener_dato(dato, "nombre")

                    if bandera_2:
                        print("no existe un clave denominada nombre o su\nvalor esta vacio")

            else:
                print("los datos no fueron normalizados")
        
        case "3":
            if bandera_1:
                while True:
                    heroe = input("""ingrese el nombre del heroe
nombre: """)

                    heroe = heroe.capitalize()

                    if heroe != "":
                        for dato in datos:
                            for valor in dato:
                                if valor == heroe:
                                    break

                        break
                    else:
                        print("no ingreso ningun nombre")

                while True:
                    dato = input("""ingrese el nombre del dato que quiera saber acerca del heroe
fuerza/ altura/ peso
dato deseado: """)
                    dato = dato.lower()
                    
                    match(dato):
                        case "fuerza":
                            break
                        case "altura":
                            break
                        case "peso":
                            break
                        case other:
                            print("esos valores no existen")

                for diccionario in datos:
                    dato_deseado, clave, nombre, bandera_3 = obtener_nombre_y_dato(diccionario, heroe, dato)

                    if bandera_3:
                        break

                if dato_deseado != None:
                    print(f"{clave}: {nombre} | {dato}: {dato_deseado}")
            else:
                print("los datos no fueron normalizados")
        
        case "4":
            if bandera_1:
                while True:
                    dato = input("""ingrese el dato del cual quiera calcular su maximo
fuerza/ peso/ altura
dato: """)

                    match(dato):
                        case "fuerza":
                            break
                        case "peso":
                            break
                        case "altura":
                            break
                        case other:
                            print("el dato que desea calcular no existe")

                maximo, bandera_4 = maximo_minimo(datos, "maximo", dato)

                if bandera_4:
                    print(f"el maximo valor de {dato}: es de {maximo}")
                else:
                    print("no se realizo nigun analisis/ los datos no estan normalizados ")
            else:
                print("Los datos no estan normalizados")
            
        case "5":
            if bandera_1:
                while True:
                    dato = input("""ingrese el dato del cual quiera calcular su minimo
fuerza/ peso/ altura
dato: """)

                    match(dato):
                        case "fuerza":
                            break
                        case "peso":
                            break
                        case "altura":
                            break
                        case other:
                            print("el dato que desea calcular no existe")

                minimo, bandera_4 = maximo_minimo(datos, "minimo", dato)

                if bandera_4:
                    print(f"el maximo valor de {dato}: es de {minimo}")

                else:
                    print("no se realizo nigun analisis/ los datos no estan normalizados ")

            else:
                print("Los datos no estan normalizados")

        case "6":
            if bandera_1:
                while True:
                    dato = input("""ingrese el dato del cual quiera calcular su maximo
fuerza/ peso/ altura
dato: """)

                    match(dato):
                        case "fuerza":
                            break
                        case "peso":
                            break
                        case "altura":
                            break
                        case other:
                            print("el dato que desea calcular no existe")

                while True:
                    analisis = input("""ingrese el analisis del cual quiera calcular su maximo
maximo/ minimo
analisis: """)

                    match(analisis):
                        case "maximo":
                            break
                        case "minimo":
                            break
                        case other:
                            print("el analisis que desea calcular no esta disponible")
            
                heroe_destacados, bandera_5 = obtener_dato_cantidad(datos, analisis, dato)

                print(f"--------------------------------------\nel/los heroe con la/el {dato} {analisis} es:")

                for diccionario in heroe_destacados:
                    print("---------------------------------")
                    for clave in diccionario:
                        print(f"{clave}: {diccionario[clave]}")
                print("-----------------------------------")

            else:
                print("los datos no estan normalizados")
        
        case "7":
            if bandera_1:
                while True:
                    dato = input("""ingrese el dato del cual quiera calcular su maximo
fuerza/ peso/ altura
dato: """)
                    
                    match(dato):
                        case "fuerza":
                            break
                        case "peso":
                            break
                        case "altura":
                            break
                        case other:
                            print("el dato que desea calcular no existe")

                promedio, bandera_6 = sacar_promedio(datos, dato)

                if bandera_6:
                    print(f"el promedio de {dato} es: {promedio}")
            else:
                print("Los datos no estan normalizados")

    os.system("pause")

    os.system("cls")
