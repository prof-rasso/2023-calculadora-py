from core.operacao import Operacao


def ler_valor(label):
    invalido = True
    while (invalido):
        try:
            return float(input(label))
        except ValueError:
            print("O valor informado é inválido!")


def ler_sim_nao(label):
    invalido = True
    continuar = None
    while (invalido):
        try:
            continuar = int(input(label))
            invalido = continuar not in range(1, 3)
        except ValueError:
            print("O valor informado é inválido!")

        if invalido:
            print("O valor informado é inválido")

    return continuar == 1


def ler_operacao():
    invalido = True
    operacao = None
    while invalido:
        print("Escolha uma operação.")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")

        try:
            operacao = Operacao.of(int(input()))
            invalido = operacao is None
        except Exception:
            pass

        if invalido:
            print("O valor informado é inválido.")

    return operacao
