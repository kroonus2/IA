import PySimpleGUI as sg
import numpy as np
import madaline as md
from targets import Targets

# Defina o cabeçalho
header = [
    sg.Text('Tabela 01', pad=(0, 0), size=(10, 2), justification='c'),
    sg.Text('Letra inserida', pad=(0, 0), size=(10, 2), justification='c'),
]

# Defina as células das tabelas
coluna1 = []
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
          'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Adicione as células das tabelas
for row in range(0, 8):
    coluna1.append([
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 0)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 1)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 2)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 3)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 4)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 5)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 6)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 7))
    ])
combo_letras = sg.Combo(letras, size=(5, len(letras)),
                        enable_events=True, key='-LETRA-', default_value='A')

layout = [
    [header, sg.Column(coluna1, element_justification='c'), combo_letras]
]

layout.append([sg.Button("Add Letra"), sg.Button("Salvar Letras"), sg.Button("Treinar"), sg.Button(
    "Testar"), sg.Button("Limpar")])

# Crie a janela
window = sg.Window("Planilhas 8x8 - Madaline",
                   layout, element_justification='c')


def pegar_Valores(colunas):
    valores_matrizes = []

    for tabela in colunas:
        for row in range(8):
            for column in range(8):
                valores_matrizes.append(
                    1 if tabela[row][column].get().strip() else -1)

    return valores_matrizes


# Listas para armazenar os vetores a serem salvos
entradas_a_serem_salvas = []
targets_a_serem_salvos = []

# Loop de eventos
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Fechar":
        break
    elif event == 'Add Letra':
        vetor_tabela1 = pegar_Valores([coluna1])
        entradas_a_serem_salvas.append(vetor_tabela1)
        letra_selecionada = values['-LETRA-']
        target_letra = Targets[letra_selecionada].value
        targets_a_serem_salvos.append(target_letra)
        sg.popup_ok("\nLetra adicionada com sucesso!")
    elif event == 'Salvar Letras':
        # Converter a lista de vetores em uma matriz numpy
        entradas_a_serem_salvas = np.array(entradas_a_serem_salvas)
        # Abre o arquivo 'entradas.txt' em modo de escrita e adiciona os vetores formatados
        with open('D:\\IA\\Madaline\\dados\\entradas.txt', 'a') as arquivo:
            for vetor in entradas_a_serem_salvas:
                vetor_str = ' '.join(str(x) for x in vetor)
                arquivo.write(vetor_str + '\n')
            # Adiciona uma linha em branco entre cada letra
            arquivo.write('\n')
        # Salvar os targets em 'targs.txt'
        with open('D:\\IA\\Madaline\\dados\\targs.txt', 'a') as arquivo:
            for target in targets_a_serem_salvos:
                arquivo.write(target + '\n')
            arquivo.write('\n')
        sg.popup_ok("\nLetra salva com sucesso!")
    # No evento 'Treinar'
    elif event == 'Treinar':
        rede_treinada = md.treinamento()
        sg.popup_ok("Rede em treinamento...")
        if rede_treinada:
            sg.popup_ok("Rede treinada com sucesso!")
        else:
            sg.popup_ok("A rede não convergiu ou atingiu o limite de ciclos.")
    elif event == 'Testar':
        vetor_teste = pegar_Valores([coluna1])
        resultado = md.teste(vetor_teste)
        print(vetor_teste)
        letra_resultado = ''
        for target in Targets:
            target_array = np.array([int(x) for x in target.value.split(';')])
            if np.all(resultado == target_array):
                letra_resultado = target.name
                break
        sg.popup_ok(f'O resultado é a letra: {letra_resultado}')
    elif event == 'Limpar':
        for row in range(8):
            for column in range(8):
                window[(row, column)].update('')

# Feche a janela
window.close()
