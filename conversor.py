valor_dolar = 724.40
valor_uf = 29356.90
valor_euro = 854.89


def conversor(opcion, moneda):
    pesos = input("¿Cuántos pesos tienes?:  ")
    pesos = float(pesos)
    resultado = pesos / moneda
    resultado = round(resultado, 2)
    resultado = str(resultado)
    return resultado


menu = """
Bienvenido al conversor de monedas 💰

==== Pesos Chilenos ====

1 - Convertir a Dólares
2 - Convertir a UF
3 - Convertir a Euros

Elige un opción:

"""

opcion = int(input(menu))

if opcion == 1:
    resultado = conversor(opcion, valor_dolar)
    print('Tienes $'+resultado+' dólares')
elif opcion == 2:
    resultado = conversor(opcion, valor_uf)
    print('Tienes '+resultado+' UF')
elif opcion == 3:
    resultado = conversor(opcion, valor_euro)
    print('Tienes '+resultado+' euros')
else:
    print('Ingresa una opción correcta')
