class persona:
    def __init__(objeto, nombre, edad):
        objeto.nombre = nombre
        objeto.edad = edad

        #just to test __name__ value
        print("__name__ when initializing persona :: %s"  %  (__name__))

    def printea(objeto):
        print("\nSe llama %s y tiene edad %d.\n"  %  (objeto.nombre, objeto.edad))


         