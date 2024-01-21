# Desafio 1
nome = input('Qual seu nome completo? \n')


def gerar_nome_completo(nome=nome):
    print(f'Bem vindo,{nome}!')


gerar_nome_completo()

# Desafio 2


def calcular_valores(preco, quantidade=1):
    total = preco * quantidade
    print(f'O preço do produto é de: \n R$ {total}.')


calcular_valores(23, 15)
