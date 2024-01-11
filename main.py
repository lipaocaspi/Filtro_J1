import os
import ui.menuP as mp
import ui.menuG as mg
import ui.menuA as ma
import ui.menuF as mf
import funciones.corefile as cf
import ui.menuPE as mpe

cf.MY_DATABASE = "data/blockbuster.json"

if __name__ == "__main__":
    isActiveApp = True
    header = """
    ****************
    *  BLOCKBUSTER *
    ****************
    """
    opMenuP = 0
    while(isActiveApp):
        os.system("cls")
        print(header)
        mp.mostrarMenuP()
        try:
            opMenuP = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Tipo de dato no válido")
        else:
            if (opMenuP == 1):
                os.system("cls")
                mg.mostrarMenuG()
            elif (opMenuP == 2):
                os.system("cls")
                ma.mostrarMenuA()
            elif (opMenuP == 3):
                os.system("cls")
                mf.mostrarMenuF()
            elif (opMenuP == 4):
                os.system("cls")
            elif (opMenuP == 5):
                os.system("cls")
                mpe.mostrarMenuPE()
            elif (opMenuP == 6):
                isActiveApp = False