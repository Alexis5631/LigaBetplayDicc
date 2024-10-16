import os
import modulos.ui as ui
import modulos.mensajes as msj
import modulos.equipos as eq
import modulos.utils as ut
import modulos.plantel as pl

if (__name__ == '__main__'):
    ligaBetplay = {}
    isActive = True
    opMenu = 0
    while (isActive):
        try:
            os.system('cls')
            print(msj.tituloMenuPrincipal)
            print(ui.menu)
            opMenu = int(input(':)_'))
            match opMenu:
                case 1:
                    isAddTeam = True
                    opMenuTeam = 0
                    while (isAddTeam):
                        try:
                            os.system('cls')
                            print(msj.tituloMenuEquipos)
                            print(ui.menuEquipos)
                            opMenuTeam = int(input(':)_'))
                        except ValueError:
                            print('Error en el dato ingresado')
                            os.system('pause')
                            continue
                        else:
                            match opMenuTeam:
                                case 1:
                                    eq.addEquipos(ligaBetplay)
                                    break
                                case 2:
                                    pass
                                case 3:
                                    isAddTeam = ut.validateData(msj.msgExitOpcion)
                                case 4:
                                    pass
                case 2:
                    iSAddPlantel = True
                    opMenuPlantel = 0
                    while (iSAddPlantel):
                        try:
                            os.system('cls')
                            print(msj.tituloMenuPlantilla)
                            print(ui.menuPlantilla)
                            opMenuPlantel = int(input(':)_'))
                        except ValueError:
                            print('Error en el dato ingresado')
                            os.system('pause')
                            continue
                        else:
                            match opMenuPlantel:
                                case 1:
                                    pass
                                case 2:
                                    pass                                   
                                case 3:
                                    iSAddPlantel = ut.validateData(msj.msgExitOpcion)
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
        except ValueError:
            print('La opcion ingresada no se encuentra en el menu')
            os.system('pause')
            continue