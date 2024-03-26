# Codigo da Inteligencia Artificial
import numpy as np

# Para porta XOR
# https://edisciplinas.usp.br/pluginfile.php/4445475/mod_resource/content/1/rn_5_mlp_1.pdf
# https://www.kaggle.com/code/alvations/xor-with-mlp


class MLP:
    def __init__(self):
        pass

    def sigmoid(x):
        return 1.0 / (1.0 + np.exp(-x))

    def sigmoid_derivada(x):
        return x * (1.0 - x)

    def tanh(x):
        return np.tanh(x)

    def tanh_derivada(x):
        return 1.0 - np.tanh(x)**2

    def treinamento(self, inputs, targets):
        epochs = 5000
        input_size = 2  # camadas de entrada
        hidden_size = 3  # camadas ocultas
        output_size = 1  # camadas de saida
        alpha = 0.1  # taxa de aprendizagem

        # Truth table
        self.inputs = inputs
        self.targets = targets

        # Preenchendo os pesos das camadas ocultas e saida com valores aleatorios
        w_hidden = np.random.uniform(size=(input_size, hidden_size))
        w_output = np.random.uniform(size=(hidden_size, output_size))

        # ciclo de aprendizagem
        for epoch in range(epochs):
            # Forward Propagation
            actual_hidden = MLP.sigmoid(np.dot(inputs, w_hidden))
            # Com tangente hiperbolica
            # actual_hidden = MLP.tanh(np.dot(inputs, w_hidden))
            output = np.dot(actual_hidden, w_output)

            # Calculando o error (saida esperada - saida obtida)
            error = targets - output

            # Backward Propagation
            dZ = error * alpha

            # peso da saida = camada oculta atual. transposta do produto escalar de dZ
            w_output += actual_hidden.T.dot(dZ)

            dH = dZ.dot(w_output.T) * MLP.sigmoid_derivada(actual_hidden)
            # Com tangente hiperbolica
            # dH = dZ.dot(w_output.T) * MLP.tanh_derivada(actual_hidden)
            w_hidden += inputs.T.dot(dH)
            print(f'epochs: {epoch+1}, error: {error}')

        return w_hidden, w_output

    def teste(self, inputs, w_hidden, w_output):
        for input in inputs:
            actual_hidden = MLP.sigmoid(np.dot(input, w_hidden))
            # Com tangente hiperbolica
            # actual_hidden = MLP.tanh(np.dot(input, w_hidden))
            actual_output = np.dot(actual_hidden, w_output)
            print(f'{input}: {actual_output}')


# Dados de treinamento e teste
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([[0], [1], [1], [0]])

# Treinamento da rede neural
mlp = MLP()
w_hidden_trained, w_output_trained = mlp.treinamento(inputs, targets)

# Teste da rede neural
print("Teste:")
mlp.teste(inputs, w_hidden_trained, w_output_trained)
