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
        
    #Função que vai retornar se os digitos são válidos ou não
    def Calculo(self):
        #Implementando o algorítimo de Luhn
        __dado1 = list()
        __dado2 = list()
        __dado3 = list()
        
        for x in self.__num[-2::-2]:
            __dado1.append(int(x)*2)

        
        for y in self.__num[-1::-2]:
            __dado2.append(int(y))   
        
        for j in __dado1:
            if j >= 10:
                m1 = j//10
                m2 = j%10
                __dado3.append(m1)
                __dado3.append(m2)            
            else:
                __dado3.append(j)
            
        n1 = sum(__dado3)    
        n2 = sum(__dado2)
        soma =(n1 + n2)
        
        if (soma % 10) == 0:
            print('=' * 50)
            print("\033[1;92mVálido\033[0;0m")


    
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
        system('clear')
        print(self.__banco)    
            




#Receber dados do usuário, interface.
class Verify:
    
    def __init__(self ):  #A ideia aqui é relacionar as classes para que não haja tratamento de dados no client/interface
        print("\033[36mSeja bem vindo ao validador de cartões.")
        print('='*35)
        self.__cardNumber = str(input("\033[30mDigite os Números do cartão(Sem espaços): "))
        
                           

        
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