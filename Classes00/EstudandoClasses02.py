'''
public, protected, private
    , _     ,    __ 
'''

import os
class BaseDeDados:

    def __init__(self):
        self.__dados = {}

    #Transformando um método em uma propriedade, para ter acesso aos dados privado 
    @property
    def Getdados(self):
        return self.__dados

    def SetClients(self, id, nome):
        if 'Clientes' not in self.__dados:
            self.__dados['Clientes'] = {id : nome}
        else:
            self.__dados['Clientes'].update({id : nome})

    def cleanClients(self, idm):
        del self.__dados ['Clientes'][idm]

    def Limpando(self): #Limpa o console
        os.system('cls')


dataBase = BaseDeDados()
dataBase.Limpando()
print("=" * 60)
dataBase.SetClients(0, "Henrique")
dataBase.SetClients(1, 'Amanda')
dataBase.SetClients(2, "Mainha") 
dataBase.__dados = "olá mundo"
#atributo renomeado para impedir que o primeiro fosse alterado
print(dataBase.__dados)
#Real atributo acesso
print(dataBase._BaseDeDados__dados)

dataBase.cleanClients(2)
print(dataBase.Getdados)