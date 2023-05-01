import math


def soma(vetor1, vetor2):
    resultado = []
    for i in range(len(vetor1)):
        resultado.append(vetor1[i] + vetor2[i])
    return resultado


def subtracao(vetor1, vetor2):
    resultado = []
    for i in range(len(vetor1)):
        resultado.append(vetor1[i] - vetor2[i])
    return resultado


def multipicacao_escalar(vetor, k):
    resultado = []
    for i in range(len(vetor)):
        resultado.append(vetor[i] * k)
    return resultado


def modulo(vetor):
    resultado = 0
    for i in range(len(vetor)):
        resultado += vetor[i] ** 2
    return math.sqrt(resultado)


def produto_escalar(vetor1, vetor2):
    resultado = 0
    for i in range(len(vetor1)):
        resultado += vetor1[i] * vetor2[i]
    return resultado


def angulo_entre_vetores(vetor1, vetor2):
    produto_escalar_vetores = produto_escalar(vetor1, vetor2)
    modulo_vetor1 = modulo(vetor1)
    modulo_vetor2 = modulo(vetor2)
    cos_angulo = produto_escalar_vetores / (modulo_vetor1 * modulo_vetor2)
    return math.degrees(math.acos(cos_angulo))


vetorA = []
vetorB = []
vetorC = []

for i in range(3):
    valor_a = float(input(f"Insira o valor {i + 1} do vetor A: "))
    vetorA.append(valor_a)

for i in range(3):
    valor_b = float(input(f"Insira o valor {i + 1} do vetor B: "))
    vetorB.append(valor_b)

for i in range(3):
    valor_c = float(input(f"Insira o valor {i + 1} do vetor C: "))
    vetorC.append(valor_c)

print("Vetor A: ", vetorA)
print("Vetor B: ", vetorB)
print("Vetor C: ", vetorC)

k = float(input('Digite o valor de k: '))

while True:
    opcao = int(input('Digite uma opção:\n'
                      '1-Calcular soma entre vetores\n'
                      '2-Calcular subtração entre vetores\n'
                      '3-Calcular Multiplicao por escalar\n'
                      '4-Calcular Módulo\n'
                      '5-Calcular Produto Escalar\n'
                      '6-Calcular Angulo entre vetores\n'
                      '0 - Finalizar\n'))
    if opcao == 1:
        opcaoParaSomar = int(
            input('Quais vetores voce deseja somar?\n1-Os Tres\n2-Vetor A e B\n3-Vetor B e C\n4-Vetor A e C\n'))
        if (opcaoParaSomar == 1):
            resultado = soma(soma(vetorA, vetorB), vetorC)
        elif (opcaoParaSomar == 2):
            resultado = soma(vetorA, vetorB)
        elif (opcaoParaSomar == 3):
            resultado = soma(vetorB, vetorC)
        elif (opcaoParaSomar == 4):
            resultado = soma(vetorA, vetorC)
        resultado = [round(x, 2) for x in resultado]
        print(resultado)


    elif opcao == 2:
        opcaoParaSubtrair = int(
            input('Quais vetores voce deseja subtrair?\n1-Os Tres\n2-Vetor A e B\n3-Vetor B e C\n4-Vetor A e C\n'))
        if (opcaoParaSubtrair == 1):
            resultado = subtracao(subtracao(vetorA, vetorB), vetorC)
        elif (opcaoParaSubtrair == 2):
            resultado = subtracao(vetorA, vetorB)
        elif (opcaoParaSubtrair == 3):
            resultado = subtracao(vetorB, vetorC)
        elif (opcaoParaSubtrair == 4):
            resultado = subtracao(vetorA, vetorC)
        resultado = [round(x, 2) for x in resultado]
        print(resultado)

    elif opcao == 3:
        opcaoParaMultiplicacaoEscalar = int(input('Qual vetor voce deseja multiplicar por k?\n'
                                                  '1 - Para vetor A\n'
                                                  '2- Para vetor B\n'
                                                  '3 - Para vetor C\n'))
        if (opcaoParaMultiplicacaoEscalar == 1):
            resultado = multipicacao_escalar(vetorA, k)
        elif (opcaoParaMultiplicacaoEscalar == 2):
            resultado = multipicacao_escalar(vetorB, k)
        elif (opcaoParaMultiplicacaoEscalar == 3):
            resultado = multipicacao_escalar(vetorC, k)

        for i in range(len(resultado)):
            resultado[i] = round(resultado[i], 2)

        for i in range(len(resultado)):
            resultado[i] = round(resultado[i], 2)

        print(resultado)



    elif opcao == 4:
        opcaoParaCalcularModulo = int(input('Qual vetor voce obter o módulo\n'
                                            '1 - Para vetor A\n'
                                            '2- Para vetor B\n'
                                            '3 - Para vetor C\n'))
        if (opcaoParaCalcularModulo == 1):
            resultado = modulo(vetorA)
        elif (opcaoParaCalcularModulo == 2):
            resultado = modulo(vetorB)
        elif (opcaoParaCalcularModulo == 3):
            resultado = modulo(vetorC)
        print(round(resultado, 2))
    elif opcao == 5:
        opcaoParaCalcularProdutoEscalar = int(input('Entre quais vetores voce deseja calcular o Produto Escalar\n'
                                                    '1 - Entre A e B\n'
                                                    '2- Entre B e C\n'
                                                    '3- Entre A e C\n'))
        if (opcaoParaCalcularProdutoEscalar == 1):
            resultado = produto_escalar(vetorA, vetorB)
        elif (opcaoParaCalcularProdutoEscalar == 2):
            resultado = produto_escalar(vetorB, vetorC)
        elif (opcaoParaCalcularProdutoEscalar == 3):
            resultado = produto_escalar(vetorA, vetorC)
        print(round(resultado, 2))
    elif opcao == 6:
        opcaoParaCalcularAnguloEntreVetores = int(input('Entre quais vetores voce deseja calcular o Angulo entre os '
                                                        'Vetores\n'
                                                        '1- Entre A e B\n'
                                                        '2- Entre B e C\n'))
        if (opcaoParaCalcularAnguloEntreVetores == 1):
            resultado = angulo_entre_vetores(vetorA, vetorB)
        elif (opcaoParaCalcularAnguloEntreVetores == 2):
            resultado = angulo_entre_vetores(vetorB, vetorC)
        print(round(resultado, 2))
    elif opcao == 0:
        break
