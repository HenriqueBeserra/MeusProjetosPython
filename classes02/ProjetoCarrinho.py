from time import sleep
from marketCar import CarrinhoDeCompras, Produto
from os import name, system


stop = 0
p1=0
p2=0
carrinho = CarrinhoDeCompras()

while stop != "N":
    system('cls')
    print('='*60)
    p1 = 0
    p2 = 0
    i = 0

  

    while  i!= 1:
        print('Informe o item e o valor:')
        p1 = str(input('Item: '))
        p2 = input('Valor: ')
        print(type(p2))
        sleep(1)

        
#Validação de informação.
        if type(p1) == str and type(int(p2)) == int:
            i = 1
            system('cls')
            break
            

        else:
            system('cls')
            print("Informação inválida!")
            sleep(0.8)
            system('cls')
            continue
            
############################            

    
     
    if i == 1:
        test = Produto(p1, int(p2))
    
    carrinho.SetItens(test)    
    
    
    stop = str(input('Dejesa continuar [S][N]?\n')).upper()
    print('Adicionando...')
    sleep(0.8)

    if stop == 'N':
        break
    elif stop == 'S':
        pass
    else:
        system('cls')
        print('Informação inválida!')
        stop = str(input('Dejesa continuar [S][N]?\n')).upper()

system('cls')
carrinho.ShowCar()
print(f'Valor total : \033[1;32m{carrinho.ItemSoma()}$\033[0;0m')