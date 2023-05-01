# Ler primeiro valor
# Ler operação
# Ler segundo valor
# Realizar o cálculo
# Imprimir o resultado do cálculo v0.1.0 [✓]
# Garantir que os valores sejam informados e que sejam númericos v0.1.1
# Garantir que uma operação válida seja informada v0.1.2
# Perguntar se deseja continuar calculando ou parar de calcular v0.2.0
# Registrar os resultados
# Perguntar se deseja imprimir os ultimos resultados ao fechar o programa. v0.3.0
# Transformação em arquivos. v0.4.0
# Transformação para 'Orientação a Objetos' v1.0.0


if __name__ == '__main__':
    print('Bem-vindo a nossa maravilhosa calculadora feita em Python!!!')

    umValor = float(input("Informe um valor: "))

    print("Escolha uma operação.")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    operacao = int(input())

    outroValor = float(input("Informe outro valor: "))

    sinal = None
    resultado = None
    if operacao == 1:
        resultado = umValor + outroValor
        sinal = '+'
    elif operacao == 2:
        resultado = umValor - outroValor
        sinal = '-'
    elif operacao == 3:
        resultado = umValor * outroValor
        sinal = '*'
    elif operacao == 4:
        resultado = umValor / outroValor
        sinal = '/'

    print(f'O resultado de {umValor:.2f} {sinal} {outroValor:.2f} é igual á {resultado:.2f}')