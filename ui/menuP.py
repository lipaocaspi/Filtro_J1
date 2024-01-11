import os
import json
import funciones.blockbuster as b
import funciones.corefile as cf

menuP = ["Administrador de Generos", "Administrador de Actores", "Administrador de Formatos", "Gestor de Informes", "Gestor peliculas", "Salir"]

def mostrarMenuP():
    b.cf.checkFile(b.blockbuster)
    for i, item in enumerate(menuP):
        print(f"{i + 1} - {item}")