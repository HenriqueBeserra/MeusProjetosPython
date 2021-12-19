import os
address = str(input("Digite o endereço do arquivo: "))



def criando(address):
    
    arquivo = open(address, 'w')
    
    arquivo.close()

def Escrevendo(texto):
    arquivo = open(address, 'a')
    arquivo.write(texto)
    arquivo.close()



Escrevendo(' Bom diaaaaaa')