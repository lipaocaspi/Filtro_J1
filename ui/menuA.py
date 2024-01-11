import os
import json
import main as m
import funciones.blockbuster as b
import funciones.corefile as cf
import funciones.actores as a

menuA = ["Crear Actor", "Listar Actor", "Ir al menu principal"]

def mostrarMenuA():
    a.cf.checkFile(a.actores)
    isIncorrect = True
    opMenuA = 0
    header = """
    ****************
    *  ACTORES *
    ****************
    """
    while (isIncorrect):
        os.system("cls")
        print(header)
        for i, item in enumerate(menuA):
            print(f"{i + 1} - {item}")
        try:
            opMenuA = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Tipo de dato no válido")
        else:
            if (opMenuA == 1):
                os.system("cls")
                a.crearActor(b.blockbuster)
            elif (opMenuA == 2):
                os.system("cls")
                a.listarActores()
            elif (opMenuA == 3):
                isIncorrect = False