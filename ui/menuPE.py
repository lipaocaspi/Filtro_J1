import os
import json
import main as m
import funciones.blockbuster as b
import funciones.corefile as cf
import funciones.actores as a
import funciones.peliculas as p

menuPE = ["Agregar Pelicula", "Editar Pelicula", "Eliminar Pelicula", "Eliminar Actor", "Buscar Pelicula", "Listar todas las peliculas", "Menu Principal"]

def mostrarMenuPE():
    # a.cf.checkFile(a.peliculas)
    isIncorrect = True
    opMenuPE = 0
    header = """
    ****************
    *   PELICULAS  *
    ****************
    """
    while (isIncorrect):
        os.system("cls")
        print(header)
        for i, item in enumerate(menuPE):
            print(f"{i + 1} - {item}")
        try:
            opMenuPE = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Tipo de dato no válido")
        else:
            if (opMenuPE == 1):
                os.system("cls")
                p.agregarPelicula(b.blockbuster)
            elif (opMenuPE == 2):
                os.system("cls")
            elif (opMenuPE == 3):
                os.system("cls")
            elif (opMenuPE == 4):
                os.system("cls")
            elif (opMenuPE == 5):
                os.system("cls")
            elif (opMenuPE == 6):
                os.system("cls")
            elif (opMenuPE == 7):
                isIncorrect = False
    