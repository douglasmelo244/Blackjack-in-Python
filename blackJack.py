import random

class preparo:
    def __init__(self):
        self.baralho=[2,3,4,5,6,7,8,9,10,10,10,10,11]*4
        random.shuffle(self.baralho)
        self.cartaJogador=[]
        self.cartaMaquina=[]
        self.carta=None
        self.jogador='Jogador'
        self.maquina='Maquina'
        self.estado=True

    def pegarCarta(self):
        self.carta=random.choice(self.baralho)
        self.baralho.remove(self.carta)

    def checaAs(self,cartas):
        self.soma=sum(cartas)
        if self.soma>10 and self.carta==11:
            self.carta=1
            return self.carta

    def calculo(self,args,kwargs):
        self.total=sum(kwargs)
        if self.total>21:
            print(f'--- {args} Perdeu ---')
            self.estado=False
            
        if self.total==21:
            print(f'!!! {args} Ganhou !!!') 
            self.estado=False                
        
        
    def adicionaJogador(self):
        self.pegarCarta()
        self.checaAs(self.cartaJogador)
        self.cartaJogador.append(self.carta)
        
        
    def adicionaMaquina(self):
        self.pegarCarta()
        self.checaAs(self.cartaMaquina)
        self.cartaMaquina.append(self.carta)

    def msg(self):
        print(f'Jogador: {self.cartaJogador} soma = {sum(self.cartaJogador)}, Máquina: {self.cartaMaquina} soma = {sum(self.cartaMaquina)} ')


    def comparador(self):
        if sum(self.cartaJogador)>sum(self.cartaMaquina) and sum(self.cartaJogador)<21:
            print('!!! Parabéns, vc ganhou !!!')

        elif sum(self.cartaMaquina)>sum(self.cartaJogador) and sum(self.cartaMaquina)<21:
            
            print('!!! Desculpe, vc perdeu !!!')

        elif sum(self.cartaJogador) == sum(self.cartaMaquina):
            
            print(' EMPATOU ')                  
        

class jogando(preparo):
    def __init__(self):
        super().__init__()

    def inicio(self):
        self.adicionaJogador()
        self.adicionaMaquina()
        self.adicionaJogador()
        self.adicionaMaquina()
        print(f'Cartas do jogador: {self.cartaJogador} a soma das cartas é: {sum(self.cartaJogador)}')
        print(f'Cartas da maquina: [{self.cartaMaquina[0]}, oculta]')
        self.calculo(self.jogador,self.cartaJogador)

    def continua(self):
        while self.estado==True:
            self.pergunta=input(' H - hit   S- stand: ')
            if self.pergunta in 'Hh':
                self.adicionaJogador()
                print(f'Cartas do jogador: {self.cartaJogador} a soma das cartas é: {sum(self.cartaJogador)}')
                print(f'Cartas da maquina: [{self.cartaMaquina[0]}, oculta]')
                self.calculo(self.jogador,self.cartaJogador)

            elif self.pergunta in 'Ss':
                while sum(self.cartaMaquina)<17:
                    self.adicionaMaquina()
                    self.calculo(self.maquina,self.cartaMaquina)
                
                self.msg()
                self.comparador()
                self.estado=False 
                       

            else:
                print( 'responda com h ou s')


        


jogar=jogando()
jogar.inicio()
jogar.continua()
