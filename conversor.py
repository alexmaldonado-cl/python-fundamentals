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
    pesos = input("¿Cuántos pesos tienes?:  ")
    pesos = float(pesos)
    valor_dolar = 724.40
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    pesos = input("¿Cuántos pesos tienes?:  ")
    pesos = float(pesos)
    valor_uf = 29356.90
    dolares = pesos / valor_uf
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes " + dolares + " UF")
elif opcion == 3:
    pesos = input("¿Cuántos pesos tienes?:  ")
    pesos = float(pesos)
    valor_euro = 854.89
    dolares = pesos / valor_euro
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes " + dolares + " euros")
else:
    print('Ingresa una opción correcta')
