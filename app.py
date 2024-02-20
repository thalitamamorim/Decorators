from turtle import Turtle
t = Turtle()
t.speed(1)

def obter_distancia():
    resposta = int(input('Quantos pixels devemos movimentar para frente? \n '))
    return resposta

def rotacionar_turtle(turtle):
    movimentar_para_lado = input(
        'Rotacionar para d: direita, e: para esquerda e n:  não rotacionar: \n ')
    if movimentar_para_lado == 'd':
         rotacionar_dreita(turtle)
    elif movimentar_para_lado == 'e':
         rotacionar_esquerda(turtle)     
    
def rotacionar_dreita(turtle):
    angulo = int(input('Quanto para direita devemos rotacionar? \n '))
    t.right(angulo) 

def rotacionar_esquerda(turtle):
    angulo = int(input('Quanto para esquerda devemos rotacionar? \n '))  
    t.left(angulo)       

while True:
    if len(pedido) < max_ingredientes:
        print(f"Você ainda pode pedir {max_ingredientes-len(pedido)}.")
        print(f"Digite o número da próxima opção desejada ou 's' para sair e finalizar seu pedido.")

        contador_opcao = 0
        for ingrediente in ingredientes:
            print (f"{contador_opcao+1} - {ingrediente}")
            contador_opcao = contador_opcao + 1

        opcao = input("Qual opção deseja? ")
        if opcao == "s":
            print ("Segue o seu pedido: ")
            for ingrediente in pedido:
                print(ingrediente)
            break
        else:
            pedido.append(ingredientes.pop(int(opcao)-1))

    else:
        print ("Segue o seu pedido: ")
        for ingrediente in pedido:
            print(ingrediente)
        break
