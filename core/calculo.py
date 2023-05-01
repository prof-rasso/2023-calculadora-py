def calcular(operacao, um_valor, outro_valor):
    sinal = None
    resultado = None

    if operacao == 1:
        resultado = um_valor + outro_valor
        sinal = '+'
    elif operacao == 2:
        resultado = um_valor - outro_valor
        sinal = '-'
    elif operacao == 3:
        resultado = um_valor * outro_valor
        sinal = '*'
    elif operacao == 4:
        resultado = um_valor / outro_valor
        sinal = '/'

    return f'O resultado de {um_valor:.2f} {sinal} {outro_valor:.2f} é igual á {resultado:.2f}'
