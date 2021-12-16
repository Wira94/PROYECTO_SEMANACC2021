from math import pow

class Circulo:
    
    def __init__(self,radio):
        self.__radio = radio
    
    PI = 3.141516
    
    def getRadio(self):
        return self.__radio
    
    def setRadio(self,radio):
        self.__radio = radio
        
    def area(self):
        return self.PI*pow(self.__radio,2)
    
    def longitudCircunferencia(self):
        return 2*self.PI*self.__radio