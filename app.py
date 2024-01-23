# Desafio decorators
from datetime import datetime


def verificar_horario(funcao):
    def visualizacao():
        now = datetime.now()
        print(datetime.now())
        funcao()
        print(datetime.now())
    return visualizacao


def mensagem():
    print('Desafio encerrado!')


resultado = verificar_horario(mensagem)
resultado()
