import os
import numpy as np
import random as rd


def carregarArquivo():
    # Puxar o arquivo txt com as inumeras letras possiveis inseridas pelo usuario
    os.chdir(r'C:\\Users\\CAUPT - ALUNOS\\Documents\\ExemploMadaline')
    entAux = np.loadtxt('Ent.txt')
    # Serão 7 letras de 63 entradas cada.
    (padroes, entradas) = np.shape(entAux)
    targAux = np.loadtxt('Targ.csv', delimiter=';', skiprows=0)
    (numSaidas, targets) = np.shape(targAux)  # Teremos 7 saídas.
    return entAux, padroes, entradas, targAux, numSaidas


def treinamento(entAux, padroes, entradas, targAux, numSaidas):
    limiar = 0.0
    alfa = 0.01
    errotolerado = 0.01
    v = np.zeros((entradas, numSaidas))  # Pesos[63][7]
    for i in range(entradas):
        for j in range(numSaidas):
            v[i][j] = rd.uniform(-0.1, 0.1)

    v0 = np.zeros((numSaidas))  # V0[7] Um bias para cada saída.
    for j in range(numSaidas):
        v0[j] = rd.uniform(-0.1, 0.1)

    # Saídas calculadas pela rede.
    yin = np.zeros((numSaidas, 1))
    y = np.zeros((numSaidas, 1))

    erro = 1
    ciclo = 0

    while erro > errotolerado:
        ciclo = ciclo + 1
        erro = 0
        for i in range(padroes):
            # Um padrão completo (letra) será arrancado.
            padraoLetra = entAux[i, :]

            for m in range(numSaidas):
                soma = 0
                for n in range(entradas):
                    soma = soma + padraoLetra[n]*v[n][m]  # Entrada x peso.
                yin[m] = soma + v0[m]

            for j in range(numSaidas):
                if yin[j] >= limiar:
                    y[j] = 1.0
                else:
                    y[j] = -1.0

            for j in range(numSaidas):
                erro = erro + 0.5*((targAux[j][i]-y[j])**2)

            vanterior = v

            for m in range(entradas):
                for n in range(numSaidas):
                    v[m][n] = vanterior[m][n]+alfa * \
                        (targAux[n][i]-y[n])*padraoLetra[m]

            v0anterior = v0

            for j in range(numSaidas):
                v0[j] = v0anterior[j] + alfa*(targAux[j][i]-y[j])

        print(ciclo)
        print(erro)


def testar(entAux, numSaidas, entradas, v, v0):
    limiar = 0.0
    yin = np.zeros((numSaidas, 1))
    y = np.zeros((numSaidas, 1))
    entTeste = entAux[6, :]
    for j in range(numSaidas):
        soma = 0
        for i in range(entradas):
            soma = soma + entTeste[i]*v[i][j]
        yin[j] = soma + v0[j]

    print(yin)
    for j in range(numSaidas):
        if yin[j] >= limiar:
            y[j] = 1.0
        else:
            y[j] = -1.0
    print(y)


# Carregamento dos arquivos
entAux, padroes, entradas, targAux, numSaidas = carregarArquivo()

# Treinamento
treinamento(entAux, padroes, entradas, targAux, numSaidas)

# Teste
v = np.zeros((entradas, numSaidas))  # Pesos[63][7]
for i in range(entradas):
    for j in range(numSaidas):
        v[i][j] = rd.uniform(-0.1, 0.1)
v0 = np.zeros((numSaidas))  # V0[7] Um bias para cada saída.
for j in range(numSaidas):
    v0[j] = rd.uniform(-0.1, 0.1)
testar(entAux, numSaidas, entradas, v, v0)
