import math
# Arquivo para calculo  de posições do braço, utilizando a lei dos cossenos

# Tamanhos em centimetros
_tamHasteInf = 50
_tamHasteSup = 50
_alturaMinimaDoBraco = 45

# anguloDobraSuperior -> Representa o angulo entre as duas hastes do braco
# anguloDobraInferior -> Representa o angulo entre a base do braco e a ponta do braco
# Esses angulos serao obtivos verificando as posicoes dos servos motores
def canMove(anguloDobraSuperior, anguloDobraInferior):
    # Calcula o cosseno entre as hastes do braco apartir do angulo fornecido
    cossenoSup = math.cos(math.radians(anguloDobraSuperior))
    
    # Considerando o formato do braco como um triangulo
    # usaremos a lei dos cossenos para calcular a distancia entre as pontas das hastes do Braco.
    # Para maior entendimento da formula estudar sobre a lei dos cossenos
    # com essa formula e possivel descobrir o tamanho do terceiro lado de um triangulo.
    distEntrePontaePontoBase = math.sqrt(( (_tamHasteInf ** 2) + (_tamHasteSup ** 2) - (2 * _tamHasteInf * _tamHasteSup * cossenoSup ))) 

    # Calculando a altura atual para validar se pode realizar um movimento na direção informada
    # Essa validacao ira verificar se altura da ponta do braco atende a altura minima em relação ao eixo da base do braco
    # assim usando a formula  Seno(angulo) = Cateto Oposto / pela hipotenusa e sabendo que a ditancia entre a base do braco e a ponta
    # sempre será a hipotenusa (variavel "distEntrePontaePontoBase"), por ser o lado maior, podemos definir a distancia da ponta do braco 
    # e a linha do do eixo da base.
    senoInf = math.sin(math.radians(anguloDobraInferior))
    # Essa (distEntrePontaeEixo) variavel pode ser considerada o cateto oposto, para maior entendimento estudade sobre pitagoras
    distEntrePontaeEixo = senoInf * distEntrePontaePontoBase

    if distEntrePontaeEixo > _alturaMinimaDoBraco: 
        Retorno = {'canMove': True, 'alturaMinimaDoBraco': _alturaMinimaDoBraco, 'distEntrePontaeEixo': distEntrePontaeEixo, 'tamHasteInf': _tamHasteInf, 'tamHasteSup': _tamHasteSup, 'senoInf': senoInf, 'cossenoSup': cossenoSup}
        return Retorno
    else:
        Retorno = {'canMove': False, 'alturaMinimaDoBraco': _alturaMinimaDoBraco, 'distEntrePontaeEixo': distEntrePontaeEixo, 'tamHasteInf': _tamHasteInf, 'tamHasteSup': _tamHasteSup, 'senoInf': senoInf, 'cossenoSup': cossenoSup}
        return Retorno