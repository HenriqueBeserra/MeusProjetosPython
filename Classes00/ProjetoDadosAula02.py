
import os 
from random import choice
from time import sleep

class DataBase:
    def __init__(self):
        self.__dados = list()
    
    @property
    def GetDados(self):
        return self.__dados
    
    #Adiciona os participantes no dicionário.
    def SetClients(self, nome, idade):
        if nome not in self.__dados:
            self.__dados.append({nome : idade})
        else:
            self.__dados.update({nome:idade})

    def CleanClients(self, nome):
        del self.__dados[nome]

    def Cls(self):
        os.system('cls')

    def Escolha(self):
        res = list()
        for nome in self.__dados:
            
            res.append(nome)
            
        return choice(res)

    def telaInit(self):
        print('=' * 60)
        print(f'As pessoas a serem selecionadas para a atividade são:\n {self.__dados}')
        
        print('=' * 60)




#Instancia da clase e execução dos métodos
bd = DataBase()
bd.Cls()
bd.SetClients('Robério', 30)
bd.SetClients('Henrique', 22)
bd.SetClients('Mainha', 50)
bd.SetClients('Painho', 40)
bd.telaInit()


#Resolução final da atividade 
select = bd.GetDados
fim = bd.Escolha()

print("Digite [1] para sortear.")
n1 = int(input(''))

if n1 == 1:
    for name in fim:
        sleep(2)
        bd.Cls()
        print(f'A pessoa selecionada para o serviço foi: \033[32m{name}')


