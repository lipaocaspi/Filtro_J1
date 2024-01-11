import os
import json
import main as m
import funciones.blockbuster as b
import funciones.corefile as cf
import funciones.generos as g

menuG = ["Crear Genero", "Listar Generos", "Ir al menu principal"]

def mostrarMenuG():
    g.cf.checkFile(g.generos)
    isIncorrect = True
    opMenuG = 0
    header = """
    ****************
    *   GENEROS    *
    ****************
    """
    while (isIncorrect):
        os.system("cls")
        print(header)
        for i, item in enumerate(menuG):
            print(f"{i + 1} - {item}")
        try:
            opMenuG = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Tipo de dato no válido")
        else:
            if (opMenuG == 1):
                os.system("cls")
                g.crearGenero(b.blockbuster)
            elif (opMenuG == 2):
                os.system("cls")
                g.listarGeneros()
            elif (opMenuG == 3):
                isIncorrect = False