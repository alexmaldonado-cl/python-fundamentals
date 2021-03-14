# contador = 1
# print(str(contador))
# while contador < 1000:
#     contador += 1
#     print(str(contador))

# a = range(1, 1000)
# print(a)

# for contador in range(1, 1001):
#     print(contador)


def tablas_multiplicacion():
    header = """

        -------------------------
        Tablas de Multiplicación
        -------------------------

    """

    print(header)

    for i in range(1, 10):
        print()
        print("==================")
        print("   TABLA DEL ", i)
        print("==================")

        for j in range(1, 10):
            print(f"{i} x {j} = " + str(i*j))


if __name__ == '__main__':
    tablas_multiplicacion()
