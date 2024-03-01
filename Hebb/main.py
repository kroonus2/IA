import PySimpleGUI as sg
import aprendizadoDeHebb

# aprendizadoDeHebb.AprendizadoHebb()

# Defina o cabeçalho
header = [
    sg.Text('Tabela 01', pad=(0, 0), size=(10, 2), justification='c'),
    sg.Text('Tabela 02', pad=(0, 0), size=(10, 2), justification='c')
]

# Defina as células das tabelas
coluna1 = []
coluna2 = []

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
    coluna2.append([
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 0 + 8)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 1 + 8)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 2 + 8)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 3 + 8)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 4 + 8)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 5 + 8)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 6 + 8)),
        sg.Input(size=(3, 1), pad=(0, 0), key=(row, 7 + 8))
    ])


layout = [
    [header, sg.Column(coluna1, element_justification='c'),
     sg.Column(coluna2, element_justification='c')]
]

layout.append([sg.Button("Treinar"), sg.Button(
    "Testar"), sg.Button("Limpar Tabela 1")])

# Crie a janela
window = sg.Window("Planilhas 8x8", layout, element_justification='c')


def pegar_Valores(colunas):
    valores_matrizes = []

    for tabela in colunas:
        for row in range(8):
            for column in range(8):
                valores_matrizes.append(
                    1 if tabela[row][column].get().strip() else -1)

    return valores_matrizes


# Loop de eventos
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Fechar":
        break
    elif event == 'Treinar':
        vetor_tabela1 = pegar_Valores([coluna1])
        vetor_tabela2 = pegar_Valores([coluna2])

        resultado = aprendizadoDeHebb.treinamentoHebb(
            vetor_tabela1, vetor_tabela2)
        sg.popup_ok(resultado + "\nPara testar use a Tabela 1")
    elif event == 'Testar':
        vetor_tabela1 = pegar_Valores([coluna1])
        resultado = aprendizadoDeHebb.testeHebb(vetor_tabela1)
        sg.popup_ok(resultado)
    elif event == 'Limpar Tabela 1':
        for row in range(8):
            for column in range(8):
                window[(row, column)].update('')

# Feche a janela
window.close()
