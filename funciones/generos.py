import os
import funciones.blockbuster as b
import funciones.corefile as cf

cf.MY_DATABASE = "data/generos.json"

generos = {
    "genero" : {
        "id" : "",
        "nombre": ""
    }
}

def crearGenero(blockbuster : dict):
    nombre = ""
    while (nombre == ""):
        nombre = input(f"Ingrese nombre del género : ")
    genero = {
        "id" : f"G{str(len(generos["genero"]) - 1).zfill(2)}",
        "nombre": nombre
    }
    generos.update({genero["id"] : genero})
    cf.UpdateFile(blockbuster)

def listarGeneros():
    print(generos)
    os.system("pause")