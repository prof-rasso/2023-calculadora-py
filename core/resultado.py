resultados = []


def registrar(resultado):
    resultados.append(resultado)


def imprimir():
    for resultado in resultados:
        print(resultado)


class Resultado:
    def __init__(self, sinal, um_valor, outro_valor, resultado):
        self.__valor = f'O resultado de {um_valor:.2f} {sinal} {outro_valor:.2f} é igual á {resultado:.2f}'

    def __str__(self):
        return self.__valor
