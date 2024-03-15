import os
import numpy as np
import random as rd

# Carregamento das entradas.
entAux = np.loadtxt('D:\\IA\\Madaline\\dados\\entradas.txt')
padroes, entradas = entAux.shape

# Carregamento das saídas.
targAux = np.loadtxt(
    'D:\\IA\\Madaline\\dados\\targs.txt', delimiter=';', skiprows=0)
numSaidas = targAux.shape[1]  # Pegar o tamanho da segunda dimensão

limiar = 0.0
alfa = 0.001
v = np.random.uniform(-0.1, 0.1, (entradas, numSaidas))  # Pesos[63][7]
# V0[7] Um bias para cada saída
v0 = np.random.uniform(-0.1, 0.1, numSaidas)

# Saídas calculadas pela rede.
yin = np.zeros((numSaidas, 1))
y = np.zeros((numSaidas, 1))


def treinamento():
    global entAux, padroes, entradas, targAux, numSaidas, yin, y, limiar, v, v0

    errotolerado = 0.9

    erro = 1
    ciclo = 0
    while erro > errotolerado and ciclo < 1000:
        ciclo += 1
        erro = 0
        for i in range(padroes):
            padraoLetra = entAux[i, :]

            for m in range(numSaidas):
                soma = 0
                for n in range(entradas):
                    soma += padraoLetra[n] * v[n][m]
                yin[m] = soma + v0[m]

            # usando degrau - rede não coverge - problema por conta do degrau
            # for j in range(numSaidas):
            #     if yin[j] >= limiar:
            #         y[j] = 1.0
            #     else:
            #         y[j] = -1.0

            # usando tangente hiberbolica - rede converge
            y = np.tanh(yin)

            for j in range(numSaidas):
                erro += 0.5 * ((targAux[i][j] - y[j]) ** 2)

            vanterior = v.copy()
            for m in range(entradas):
                for n in range(numSaidas):
                    v[m][n] = vanterior[m][n] + alfa * \
                        (targAux[i][n] - y[n]) * padraoLetra[m]
            v0anterior = v0.copy()
            for j in range(numSaidas):
                v0[j] = v0anterior[j] + alfa * (targAux[i][j] - y[j])
        print(f'ciclo:: {ciclo}')
        print(f'erro:: {erro}')

    return erro <= errotolerado or ciclo >= 1000


def teste(entTeste):
    global entradas, numSaidas, v, v0
    # Teste
    # Rede treinada com sucesso.
    for j in range(numSaidas):
        soma = 0
        for i in range(entradas):
            soma = soma + entTeste[i]*v[i][j]
        yin[j] = soma + v0[j]

    # for j in range(numSaidas):
    #     if yin[j] >= limiar:
    #         y[j] = 1.0
    #     else:
    #         y[j] = -1.0

    # usando tangente hiberbolica - rede converge
    y = np.tanh(yin)

    # Padronizando as saidas
    for j in range(26):
        if y[j] >= 0:
            y[j] = 1.0
        else:
            y[j] = -1.0

    print(y)
    return (y)


treinamento()

# # Teste resultado
print('Teste A')
teste(([-1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -
      1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1]))

# Teste resultado B
print('Teste B')
teste(([1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1,
      1, -1, 1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1]))

# Teste C
print('Teste C')
teste(([-1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1,
      1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1]))

# Teste E
print('Teste E')
teste(([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -
      1, -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1]))

# Teste F
print('Teste F')
teste(([1, 1, -1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1,
      1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1]))

# Teste O
print('Teste O')
teste(([-1, -1, 1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1,
      1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1]))

# Teste R
print('Teste R')
teste(([1, 1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1,
      1, 1, -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1]))
