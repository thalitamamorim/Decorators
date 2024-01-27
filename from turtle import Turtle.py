# Desafio 1
# Monte um mini-game turtle, que possibilite que o usuário controle para qual direção a tartaruga deve andar(frente/trás)
# e qual ângulo deverá ser tomado a cada nova movimentação
# Desafio 2
# Usando o mini-game, desenha um quadrado passando instruções para a turtle, totalmente através do input do usuário
from turtle import Turtle
# Importando a classe biblioteca Turtle
t = Turtle()
# Criando a Instancia da biblioteca Turlte
t.shape("turtle")
t.color("#285078", "#a0c8f0")
# Definindo a forma da tartaruga com turtle e sua cor com  azul escuro ("#285078")
# para o contorno e azul claro ("#a0c8f0") para o preenchimento.
while True:  # Iniciando o loop infinito
    # Solicitando ao usuario insira a direção f frente t para tras
    direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás"')
    if direcao == 'f':  # Logica para mover para frente
        distancia = int(
            input('Quantos pixels devemos movimentar para a frente? '))
        movimentar_para_lado = input(
            'Rotacionar para d:direta, e:esquerda n:não rotacionar ')
        if movimentar_para_lado == 'd':
            # Solicita ao usuario quanto rotacionar
            angulo = int(input('Quanto para a direta devemos rotacionar? '))
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar? '))
            t.left(angulo)
        t.forward(distancia)
    if direcao == 't':
        distancia = int(
            input('Quantos pixels devemos movimentar para a trás? '))
        movimentar_para_lado = input(
            'Rotacionar para d:direta, e:esquerda n:não rotacionar ')
        if movimentar_para_lado == 'd':
            angulo = int(input('Quanto para a direta devemos rotacionar? '))
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar? '))
            t.left(angulo)
        t.backward(distancia)
    # Verificação para continuar ou parar
    resposta = input('Continuar andando? ')
    if resposta not in ('sim', 's'):
        break
