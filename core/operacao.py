from enum import Enum

from core import calculo


class Operacao(Enum):
    SOMA = 1
    SUBTRACAO = 2
    MULTIPLICACAO = 3
    DIVISAO = 4

    @staticmethod
    def of(operacao):
        for i in Operacao:
            if i.value == operacao:
                return i

        raise Exception("Operação inválida")

    def criar_novo_calculo(self, um_valor, outro_valor):
        if Operacao.SOMA == self:
            return calculo.Soma(um_valor, outro_valor)
        elif Operacao.SUBTRACAO == self:
            return calculo.Subtracao(um_valor, outro_valor)
        elif Operacao.MULTIPLICACAO == self:
            return calculo.Multiplicacao(um_valor, outro_valor)
        elif Operacao.DIVISAO == self:
            return calculo.Divisao(um_valor, outro_valor)
