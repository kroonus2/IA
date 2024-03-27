import numpy as np

# Exemplo Slide


class MLP:
    def __init__(self):
        pass

    def treinamento(self):
        inputs = np.array([[[1, 0.5, -1]], [[0, 0.5, 1]], [[1, -0.5, -1]]])
        targets = np.array([[1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
        alpha = 0.001

        # 3 entradas, 2 camadas intermediarias
        v = np.random.uniform(size=(3, 100), low=-0.5,
                              high=0.5)  # vij # 64 / 100
        w = np.random.uniform(size=(100, 3), low=-0.5,
                              high=0.5)  # wjk # 100 / 26
        b_hidden = np.random.uniform(size=(1, 100), low=-0.5, high=0.5)  # v0j
        b_output = np.random.uniform(
            size=(1, 3), low=-0.5, high=0.5)  # w0k 1 / 26

        erro = np.Infinity
        epoch = 0

        while epoch < 100000 and erro > 0.1:
            epoch += 1
            erro = 0
            for i in range(len(inputs)):
                # ForwardPropagation
                # Camada de
                zin = np.dot(inputs[i], v)+b_hidden
                z = np.tanh(zin)
                # Camada
                yin = (np.dot(z, w)+b_output)
                y = np.tanh(yin)

                # BackPropagation
                # erro total
                deltinha_yin = targets[i] - y
                # erro da camada intermediaria
                erro += 0.5 * np.sum(deltinha_yin**2)
                # Delta Camada intermediaria
                deltinha_y = deltinha_yin * (1.0 - np.tanh(yin)**2)  # v
                # erro camada de entrada
                deltinha_zin = deltinha_y.dot(w.T)
                # Delta Camada entrada
                deltinha_z = deltinha_zin * (1.0 - np.tanh(zin)**2)  # w

                # Atualizando os pesos e bias
                delta_w = alpha * np.dot(deltinha_y.T, z)
                delta_b_W = alpha * deltinha_y
                delta_v = alpha * np.dot(deltinha_z.T, inputs[i])
                delta_b_V = alpha * deltinha_z

                w = w + delta_w.T  # wjk
                b_output = b_output + delta_b_W  # w0k
                v = v + delta_v.T  # vij
                b_hidden = b_hidden + delta_b_V  # v0j

            print("Epoch:", epoch, "Error:", erro)

        # Retornar os pesos e bias treinados
        return v, w, b_hidden, b_output

    def teste(self, inputs, v, w, b_hidden, b_output):
        outputs = []
        for input_data in inputs:
            # Camada de entrada
            z = np.tanh((np.dot(input_data, v) + b_hidden))
            # Camada intermediaria
            y = np.tanh((np.dot(z, w) + b_output))
            outputs.append(y)

        return outputs


# Teste da MLP após o treinamento
mlp = MLP()
v, w, b_hidden, b_output = mlp.treinamento()

# Dados de teste
test_inputs = [[1, 0.5, -1], [0, 0.5, 1], [1, -0.5, -1]]

# Realizar o teste
test_outputs = mlp.teste(test_inputs, v, w, b_hidden, b_output)
print("Outputs após o teste:")
for output in test_outputs:
    print(output)
