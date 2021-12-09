
from time import sleep

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def GetNome(self):
        return self.__nome

    @property
    def GetFerramenta(self):
        return self.__ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def GetCaneta(self):
        return self.__marca


class WiriteMachine:
    def Escrever(self, txt):
        print("Machine writing...")
        sleep(2)
        print(txt)
    




        
        