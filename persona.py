class persona:
    def __init__(objeto, nombre, edad):
        objeto.nombre = nombre
        objeto.edad = edad
        #print("__name__ when running __init__ persona :: %s"  %  (__name__))

    def printea(objeto):
        print("\nSe llama %s y tiene edad %d.\n"  %  (objeto.nombre, objeto.edad))


         