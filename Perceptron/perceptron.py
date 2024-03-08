import numpy as np


def treinamento(input, target, max_iter=100):
    limiar = 0
    # Initialize weights with the same length as the number of features
    w = np.random.rand(input.shape[1])
    b = 0.6
    print(f'wInicial:{w} - bInicial:{b}')
    alfa = 0.1  # Learning rate

    for _ in range(max_iter):
        erro = False
        for i in range(len(input)):
            # Cálculo da saída líquida
            y_liq = np.dot(input[i], w) + b
            # Ativação da função de passo
            y = 1 if y_liq >= limiar else 0
            # Atualização dos pesos e bias se houver erro
            if y != target[i]:
                erro = True
                w += alfa * (target[i] - y) * input[i]
                b += alfa * (target[i] - y)
        if not erro:
            break

    return w, b


def andGate():
    input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([0, 0, 0, 1])
    w, b = treinamento(input, target)  # Chamada sem max_iter
    y = [int(np.dot(input[i], w) + b >= 0) for i in range(len(input))]
    return y, w, b


def orGate():
    input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([0, 1, 1, 1])
    w, b = treinamento(input, target)  # Chamada sem max_iter
    y = [int(np.dot(input[i], w) + b >= 0) for i in range(len(input))]
    return y, w, b


def nandGate():
    input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([1, 1, 1, 0])
    w, b = treinamento(input, target)  # Chamada sem max_iter
    y = [int(np.dot(input[i], w) + b >= 0) for i in range(len(input))]
    return y, w, b


def norGate():
    input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([1, 0, 0, 0])
    w, b = treinamento(input, target)  # Chamada sem max_iter
    y = [int(np.dot(input[i], w) + b >= 0) for i in range(len(input))]
    return y, w, b


def xorGate():
    input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([0, 1, 1, 0])  # Correct target values for XOR
    w, b = treinamento(input, target)  # Chamada sem max_iter
    y = [int(np.dot(input[i], w) + b >= 0) for i in range(len(input))]
    return y, w, b
