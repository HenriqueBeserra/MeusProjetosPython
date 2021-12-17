#Source Code 
#Classes que verificam a bandeira e validam o número do cartão.
from os import system

class Card:
    #Recebe os atributos e os transforma em string para validações.
    def __init__(self):
        self.__num = []
        self.__banco = str()
        #Dados dos bancos 
        self.__Master = ["51", "52", "53", "54", '55']
        self.__American = ["34", '37']
        self.__Visa = ["4"]
    
    #Função que vai se ligar com a interface e coletar os digitos do cartão
    def Ban(self,num):
        
        self.__num = str(num)
        
    
    def Calculo(self):
        #Implementando o algorítimo de Luhn
        __dado1 = list()
        __dado2 = list()
        for x in self.__num[-2::-2]:
            #__dado1.append(int(x))
            print(x)
        for y in self.__num[-1::-2]:
            print(y)   


        

    #Função que identifica o banco.
    def Banco(self):

        
        if self.__num[0:2] in self.__American:
            self.__banco = "BANCO: American Express"
            
           
        elif self.__num[0:2] in self.__Master:
            self.__banco = "BANCO: MasterCard"
            
        
        elif self.__num[0:1] in self.__Visa :
            self.__banco = "BANCO: Visa"
        
            
        else:
            self.__banco = ("Número inválido. \nError.01 \Curto||Longo")
        
        
    def Show(self):
        system('cls')
        print(self.__banco)    
            




#Receber dados do usuário
class Verify:
    
    def __init__(self ):  #A ideia aqui é relacionar as classes para que não haja tratamento de dados no client/interface
        self.__cardNumber = str(input("Digite os digitos do cartão(Sem espaços): "))
        
                           

        
    def Valid(self):
    
        carro = Card()
        carro.Ban(self.__cardNumber)
        carro.Banco()
        carro.Show()
        carro.Calculo()


""""
Base de informações: 

teste = []
teste  = str(123422353457)
teste.split()
print(teste)

print(teste[0])
soma = 0
i = 0
for item in teste:
    
    soma = soma + int(item)
    i+=1

print(teste[-2::-2])
"""