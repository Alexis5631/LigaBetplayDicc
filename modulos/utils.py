def validateData(message:str):
    flagfunction = True
    opciones = ('N','n','S','s')
    accion = input(f'{message}')
    if (accion not in opciones):
        print('La opcion que usted ingreso no es valida....')
        validateData()
    elif (accion == 'N'):
        flagfunction = True
    elif ((accion) == 'S'):
        flagfunction = False
    return flagfunction