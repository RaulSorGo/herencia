from math import pi


class Forma():
    
    def area(self):
        pass

    def perimetro(self):
        pass

    def __str__(self) -> str:
        return type(self).__name__

class Circulo(Forma):
    def __init__(self,radio) -> None:
        self.__radio = radio

    def area(self):
        return pi * self.__radio * self.__radio

    def perimetro(self):
        return 2 * pi * self.__radio
