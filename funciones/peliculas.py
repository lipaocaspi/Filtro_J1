import os
import funciones.corefile as cf

peliculas = {
    "peliculas": {
        "id": "",
        "nombre": "",
        "duracion": "",
        "sinopsis": "",
        "generos": {},
        "actores" : {},
        "formato": {}
    }
}

def verificarDato(enunciadoDato : str) -> str:
    dato = ""
    while (dato == ""):
        dato = input(enunciadoDato)
    return dato


def agregarPelicula(blockbuster : dict):
    nombre = verificarDato("Ingrese nombre de la pelicula : ")
    duracion = verificarDato("Ingrese duracion de la pelicula : ")
    sinopsis = verificarDato("Ingrese sinopsis de la pelicula : ")

    pelicula = {
        "id": f"P{str(len(peliculas["pelicula"] - 1)).zfill(2)}",
        "nombre": nombre,
        "duracion": duracion,
        "sinopsis": sinopsis,
        "generos": {},
        "actores" : {},
        "formato": {}
    }

    peliculas.update({pelicula["id"] : pelicula})
    blockbuster["blockbuster"]["peliculas"].update({pelicula["id"] : pelicula})
    cf.UpdateFile(blockbuster)