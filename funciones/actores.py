import os
import funciones.blockbuster as b
import funciones.corefile as cf

cf.MY_DATABASE = "data/actores.json"

actores = {
    "actor" : {
        "id" : "",
        "nombre": ""
    }
}

def crearActor(blockbuster : dict):
    nombre = ""
    while (nombre == ""):
        nombre = input(f"Ingrese nombre del actor : ")
    actor = {
        "id" : f"A{str(len(actores["actor"]) - 1).zfill(2)}",
        "nombre": nombre
    }
    actores.update({actor["id"] : actor})
    cf.UpdateFile(blockbuster)

def listarActores():
    print(actores)
    os.system("pause")