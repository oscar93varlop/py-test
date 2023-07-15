# coding=utf-8
with open("resultado.txt", "w") as archivo:
    for elemento in range(1, 51):
        if elemento % 2 == 0:
            mensaje = "El número {} es par \n".format(elemento)
        else:
            mensaje = "El número {} es impar \n".format(elemento)
        archivo.write(mensaje)
