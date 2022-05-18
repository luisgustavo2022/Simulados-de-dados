import random
class SimuladorDeDado:
    def __init__(self):
        self.mensagem = 'você gostaria de gerar um novo valor para o dado? '

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
               vezes = int(input('quer gerar com quantos dados?'))
               self.minimo = vezes
               self.maximo = 6 * vezes
               self.gerar(self.minimo, self.maximo)


            elif resposta == 'não' or resposta == 'n':
                print('obrigado pela participação')
            else:
                print('digite sim ou não!!!')
        except:
            print('Ocorreu um erro')

    def gerar(self, minimo, maximo):
        print(random.randint(self.minimo, self.maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
