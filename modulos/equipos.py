import os
import modulos.utils as uc


def addEquipos (lstLiga:dict):
    
    isAddEquipo = True
    while(isAddEquipo):
        os.system('cls')
        nombreEquipo = input("Ingrese el nombre del equipo: ")
        if nombreEquipo not in lstLiga:
            lstLiga[nombreEquipo] = {}
            print(f"Equipo '{nombreEquipo}' agregado a la liga.")
            isAddEquipo = uc.validateData("¿Desea agregar otro equipo? (S/N): ")
        else:
            print(f"El equipo '{nombreEquipo}' ya existe en la liga.")
