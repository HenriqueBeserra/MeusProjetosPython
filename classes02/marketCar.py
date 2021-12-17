#Associando classes 
#onde a classe carrinho depende da produto, mas não ao contrário
from time import sleep
import os
class CarrinhoDeCompras:
    def __init__(self):
        self.__item = []

    
    def SetItens(self, produto):
        self.__item.append(produto)
    
    

    def ShowCar(self):
        print('Seu carrinho:')
        print('='*20)    
        for item in self.__item:
            print(str(item.nome).capitalize(), f"\033[1;36m{item.valor}\033[0;0m" )
        print('='*20)   
           
    
    def ItemSoma(self):
        total = 0
        for itens in self.__item:
            total += itens.valor
        return total





class Produto:
    def __init__(self, Nome, valor):
        self.nome = Nome
        self.valor = valor 





               
        
            
            

    



  





