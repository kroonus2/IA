# Codigo da Inteligencia Artificial
import numpy as np

# Para porta XOR
# https://edisciplinas.usp.br/pluginfile.php/4445475/mod_resource/content/1/rn_5_mlp_1.pdf
# https://gist.github.com/Jalalx/a9051b325f066faae6572dae1180baa1
# https://www.kaggle.com/code/alvations/xor-with-mlp


class MLP:
    def __init__(self) -> None:
        pass

    def treinamento(self, inputs, outputs, alpha, epochs):
        self.inputs = inputs
        self.outputs = outputs
        self.alpha = alpha  # taxa de aprendizado do algoritmo
        self.epochs = epochs  # numero de iterações na etapa de treinamento

        # Neste bloco definimos os pesos e bias que serão inicializados aletatoriamente entre 0 e 1
        w11 = np.random.uniform(0, 1)
        w12 = np.random.uniform(0, 1)
        w21 = np.random.uniform(0, 1)
        w22 = np.random.uniform(0, 1)

        wh1 = np.random.uniform(0, 1)
        wh2 = np.random.uniform(0, 1)

        b1 = np.random.uniform(0, 1)
        b2 = np.random.uniform(0, 1)
        b3 = np.random.uniform(0, 1)

        # Iniciação dos laços de repetições do treinamento
        for i in range(epochs):
            for j in range(len(inputs)):
                # Camada de entrada - Por Sigmoid
                h1 = 1 / \
                    (1 + np.exp(- ((inputs[j][0] * w11) +
                     (inputs[j][1] * w21) + b1)))
                h2 = 1 / \
                    (1 + np.exp(- ((inputs[j][0] * w12) +
                     (inputs[j][1] * w22) + b2)))

                # Função de Ativação
                y = 1 / (1 + np.exp(- ((h1 * wh1) + (h2 * wh2) + b3)))

                erro = outputs[j][0] - y

                # Efetuamos o cálculo das derivadas parciais
                derivative_y = y * (1 - y) * erro
                derivative_h1 = h1 * (1 - h1) * wh1 * derivative_y
                derivative_h2 = h2 * (1 - h2) * wh2 * derivative_y

                # Cálculo dos deltas que serão usados para atualização dos pesos
                delta_w11 = alpha * derivative_h1 * inputs[j][0]
                delta_w12 = alpha * derivative_h2 * inputs[j][0]
                delta_w21 = alpha * derivative_h1 * inputs[j][1]
                delta_w22 = alpha * derivative_h2 * inputs[j][1]

                delta_b1 = alpha * derivative_h1
                delta_b2 = alpha * derivative_h2
                delta_b3 = alpha * derivative_y

                delta_wh1 = alpha * derivative_y * h1
                delta_wh2 = alpha * derivative_y * h2

                # Atualizando os pesos e retornando os pesos obtidos após o treinamento
                w11 += delta_w11
                w12 += delta_w12
                w21 += delta_w21
                w22 += delta_w22

                wh1 += delta_wh1
                wh2 += delta_wh2

                b1 += delta_b1
                b2 += delta_b2
                b3 += delta_b3
                print(f'epoch - {epochs}, erro - {erro}')

            return w11, w12, w21, w22, wh1, wh2, b1, b2, b3

    def teste(self, pesos, x1, x2):
        hidden1 = 1 / \
            (1 + np.exp(- ((x1 * pesos[0]) +
             (x2 * pesos[2]) + pesos[6])))
        hidden2 = 1 / \
            (1 + np.exp(- ((x1 * pesos[1]) +
             (x2 * pesos[3]) + pesos[7])))

        # Note que nos cálculos anteriores da função sigmoid, retornávamos o valor puro, já aqui colocamos a condição necessária para retornar se o neurônio foi ativado ou não
        return 1 if 1 / (1 + np.exp(- ((hidden1 * pesos[4]) + (hidden2 * pesos[5]) + pesos[8]))) > 0.5 else 0


# Dados de entrada e saída baseados na tabela verdade usando a porta lógica XOR
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [[0], [1], [1], [0]]

mlp = MLP()
# Executamos o treinamento da rede com uma taxa de aprendizado de 5% e 10.000 épocas de treinamento
tr = mlp.treinamento(inputs, outputs, 0.05, 10000)
# Testamos o algoritmo utilizando as entradas 1 e 1, se o algoritmo foi treinado com uma taxa de aprendizado adequada e por uma quantidade razoável de épocas, iremos obter um bom resultado, mostrando que a máquina aprendeu a porta XOR
y = mlp.teste(tr, 1, 1)
print(y)
