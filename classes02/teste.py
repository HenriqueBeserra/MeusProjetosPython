from os import system
from time import sleep
p1 = 0
p2 = 0
i = 0

while  i!= 1:
    print('Informe o item e o valor:')
    p1 = str(input())
    p2 = int(input())

    print(type(p1), type(p2))
    sleep(2)


    if type(p1) == str and type(p2) == int:
        print(p1)
        i = 1
        break

    else:
        system('cls')
        print("Informação inválida!")
        sleep(0.5)
        system('cls')
        break