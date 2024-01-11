import os
import funciones.blockbuster as b
import funciones.corefile as cf

cf.MY_DATABASE = "data/formatos.json"

formatos = {
    "formato" : {
        "id" : "",
        "nombre": ""
    }
}

def crearFormato(blockbuster : dict):
    nombre = ""
    while (nombre == ""):
        nombre = input(f"Ingrese nombre del formato : ")
    formato = {
        "id" : f"F{str(len(formatos) - 1).zfill(2)}",
        "nombre": nombre
    }
    formatos.update({formatos["id"] : formato})
    cf.UpdateFile(blockbuster)

def listarFormatos():
    print(formatos)