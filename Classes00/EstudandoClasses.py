import os
#Estudando classes

class Pessoa:
   #Se comporta como um método construtor
    def __init__(self, nome, idade):
        
        #Atributos
        self.nome = nome
        self.idade = idade

    #Métodos
    def GetIdade(self):
        
        print(self.idade)
        

    def GetNome(self):
        print(self.nome)

    def SetNome(self, nom):
        self.nome = nom 

    def SetIdade(self, id):
        self.idade = id
    
    def Limpando(self): #Limpa o console
        os.system('cls')


#Instancia da classe

pessoa = Pessoa("Henrique", 22)
pessoa.Limpando()
pessoa.GetNome()
pessoa.SetIdade(29)
pessoa.GetIdade()





