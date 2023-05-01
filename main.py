# Ler primeiro valor
# Ler operação
# Ler segundo valor
# Realizar o cálculo
# Imprimir o resultado do cálculo v0.1.0 [✓]
# Garantir que os valores sejam informados e que sejam númericos v0.1.1 [✓]
# Garantir que uma operação válida seja informada v0.1.2 [✓]
# Perguntar se deseja continuar calculando ou parar de calcular v0.2.0 [✓]
# Registrar os resultados [✓]
# Perguntar se deseja imprimir os ultimos resultados ao fechar o programa. v0.3.0 [✓]
# Transformação em arquivos. v0.4.0 [✓]
# Transformação para 'Orientação a Objetos' v1.0.0
from cli import terminal
from core import resultado
from core import calculo

if __name__ == '__main__':
    print('Bem-vindo a nossa maravilhosa calculadora feita em Python!!!')
    continuar = True

    while continuar:
        um_valor = terminal.ler_valor("Informe um valor: ")
        operacao = terminal.ler_operacao()
        outro_valor = terminal.ler_valor("Informe outro valor: ")

        resultadoTxt = calculo.calcular(operacao, um_valor, outro_valor)
        print(resultadoTxt)

        resultado.registrar(resultadoTxt)

        continuar = terminal.ler_sim_nao("Deseja continuar calculando? (1-Sim,2-Não): ")

    imprimir = terminal.ler_sim_nao("Deseja imprimir os resultados? (1-Sim,2-Não): ")

    if imprimir:
        resultado.imprimir()

    print("Bye Bye!")