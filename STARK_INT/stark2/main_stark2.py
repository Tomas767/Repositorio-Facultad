from funciones_main_stark2 import *
from data import *
import os

while True:
    op = menu()

    match(op):
        case "A":
            lista_heroes = buscar(lista_personajes, "genero", "NB", "nombre")

            if lista_heroes != []:
                for heroe in lista_heroes:
                    print("los superheroes del genero no binario som:")

                    print(f"{heroe}\n-------------------------------")
            
            else:
                print("No existen heroes de ese genero")
            
        case "B":
            lista_heroes = maximo_minimo(lista_personajes, "maximo", "genero", "F", "altura", "nombre")

            if lista_heroes != []:
                print(f"las superheroinas femeninas mas altas son: ")

                for heroe in lista_heroes:
                    print(f"*{heroe}")
        case "C":
            lista_heroes = maximo_minimo(lista_personajes, "maximo", "genero", "M", "altura", "nombre")
            
            if lista_heroes != []:
                print(f"los superheroes masculinos mas altos son: ")

                for heroe in lista_heroes:
                    print(f"*{heroe}")

        case "D":
            lista_heroes = maximo_minimo(lista_personajes, "minimo", "genero", "M", "fuerza", "nombre")

            if lista_heroes != []:
                print("el superheroe mas debil del genero masculino es:")

                for heroe in lista_heroes:
                    print(heroe)
        case "E":
            lista_heroes = maximo_minimo(lista_personajes, "minimo", "genero", "NB", "fuerza", "nombre")

            if lista_heroes != []:
                print("el superheroe mas debil del genero NB es:")

                for heroe in lista_heroes:
                    print(heroe)
            else:
                print("no existen superheroes de ese genero")
        case "F":
            prom = promedio(lista_personajes, "NB", "fuerza")

            if type(prom) != str:
                print(f"""el promedio de fuerza del genero NB es:
{prom}""")
            else:
                print(prom)

        case "G":
            set_elementos = crear_set(lista_personajes, "color_ojos")

            print("La cantidad de heroes con cada tipo de color de ojos son: ")
            for elemento in set_elementos:
                contador = contavilizar(lista_personajes, elemento, "color_ojos")

                print(f"""
{elemento}: {contador}""")

        case "H":
            set_elementos = crear_set(lista_personajes, "color_pelo")

            print("La cantidad de heroes con cada tipo de color de pelo son: ")
            for elemento in set_elementos:
                contador = contavilizar(lista_personajes, elemento, "color_pelo")

                print(f"""
{elemento}: {contador}""")

        case "I":
            set_elementos = crear_set(lista_personajes, "color_ojos")

            for elemento in set_elementos:
                recorrer_set(lista_personajes,"color_ojos", elemento, 'nombre')

        case "J":
            set_elementos = crear_set(lista_personajes, "inteligencia")

            for elemento in set_elementos:
                recorrer_set(lista_personajes,"inteligencia", elemento, 'nombre')

    os.system("pause")

    os.system("cls")
