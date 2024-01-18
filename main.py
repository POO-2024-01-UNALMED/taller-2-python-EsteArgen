class Asiento:

    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if (color == "rojo" or  color == "verde" or color == "amarillo" or color == "negro" or color == "blanco"):
            self.color = color

class Motor:

    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro



    
class Auto:

    
    def cantidadAsientos (self):
        numAsientos = 0

        
    def verificarIntegridad(self):
        if (self.registro == self.motor.registro):
            for asiento in self.asientos:
                if (type(asiento) == Asiento):
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"


