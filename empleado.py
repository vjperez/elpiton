from persona import persona

class empleado(persona):
    def __init__(objeto, nombre, edad, empresa, posicion):
        persona.__init__(objeto, nombre, edad)
        objeto.empresa = empresa
        objeto.posicion = posicion

    def printea(objeto):
        persona.printea(objeto)
        print("Trabaja en %s como %s.\n"  %  (objeto.empresa, objeto.posicion))