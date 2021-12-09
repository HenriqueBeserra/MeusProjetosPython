
from testePython import  Escritor
from testePython import Caneta
from testePython import WiriteMachine

escritor = Escritor('João')
caneta = Caneta('Bic')
machine = WiriteMachine()

#enviando uma classe para dentro de um atributo para associar as classes 
escritor.__ferramenta = machine
escritor.__ferramenta.Escrever(f'{caneta.GetCaneta}, {escritor.GetNome}')


