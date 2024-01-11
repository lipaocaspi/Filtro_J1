import os
import json
import main as m
import funciones.blockbuster as b
import funciones.corefile as c
import funciones.formatos as f

menuF = ["Crear formatos", "Listar formatos", "Ir al menu principal"]

def mostrarMenuF():
    f.cf.checkFile(f.formatos)
    header = """
    ****************
    *   FORMATOS   *
    ****************
    """
    isIncorrect = True
    opMenuF = 0
    while (isIncorrect):
        os.system("cls")
        print(header)
        for i, item in enumerate(menuF):
            print(f"{i + 1} - {item}")
        try:
            opMenuF = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Tipo de dato no válido")
        else:
            if (opMenuF == 1):
                os.system("cls")
                f.crearFormato(b.blockbuster)
            elif (opMenuF == 2):
                os.system("cls")
            elif (opMenuF == 3):
                isIncorrect = False