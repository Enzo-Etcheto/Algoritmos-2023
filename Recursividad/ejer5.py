#Desarrollar una función que permita convertir un número romano en un número decimal.
nm = 'XX'

def nmromano (nmroma):
    """Funcion recursiva convertir para convertir numeros romanos en numeros decimales"""
    vromano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not nmroma:
        return 0
    else:
        if len(nmroma) == 1:
            return vromano[nmroma]
        else:
            if vromano[nmroma[0]] < vromano[nmroma[1]]:
                return vromano[nmroma[1]] - vromano[nmroma[0]] + nmromano(nmroma[2:])
            else:
                return vromano[nmroma[0]] + nmromano(nmroma[1:])

print(nm,"en numero decimal es",nmromano(nm))