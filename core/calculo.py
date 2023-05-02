from core.resultado import Resultado


class Soma:
    def __init__(self, um_valor, outro_valor):
        self.__um_valor = um_valor
        self.__outro_valor = outro_valor
        self.__resultado = um_valor + outro_valor

    def calcular(self):
        return Resultado("+", self.__um_valor, self.__outro_valor, self.__resultado)


class Subtracao:
    def __init__(self, um_valor, outro_valor):
        self.__um_valor = um_valor
        self.__outro_valor = outro_valor
        self.__resultado = um_valor - outro_valor

    def calcular(self):
        return Resultado("-", self.__um_valor, self.__outro_valor, self.__resultado)


class Multiplicacao:
    def __init__(self, um_valor, outro_valor):
        self.__um_valor = um_valor
        self.__outro_valor = outro_valor
        self.__resultado = um_valor * outro_valor

    def calcular(self):
        return Resultado("*", self.__um_valor, self.__outro_valor, self.__resultado)


class Divisao:
    def __init__(self, um_valor, outro_valor):
        self.__um_valor = um_valor
        self.__outro_valor = outro_valor
        self.__resultado = um_valor / outro_valor

    def calcular(self):
        return Resultado("/", self.__um_valor, self.__outro_valor, self.__resultado)

