import PySimpleGUI as sg
import perceptron

# Função para criar a tabela com base na operação lógica selecionada


def create_table(operation):
    if operation == "AND":
        table_data = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 1]
        ]
    elif operation == "OR":
        table_data = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    elif operation == "NAND":
        table_data = [
            [0, 0, 1],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
    elif operation == "XOR":
        table_data = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
    elif operation == "NOR":
        table_data = [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 0]
        ]
    return table_data


# Inicializar a tabela com a operação lógica "AND"
initial_table_data = create_table("AND")

# Layout da interface gráfica
layout = [
    [sg.Text("Selecione a tabela lógica:")],
    [sg.Combo(["AND", "OR", "NAND", "XOR", "NOR"],
              key="operation", default_value='AND', enable_events=True)],
    [sg.Table(values=initial_table_data, headings=["A", "B", "Resultado"],
              auto_size_columns=False, col_widths=[5, 5, 10], key="result_table"),],
    [sg.Button("Treinar Perceptron"), sg.Button("Sair")]
]

window = sg.Window("Tabela Lógica", layout)

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "Sair"):
        break

    # Atualizar os valores da tabela com base na operação selecionada
    if "operation" in event:
        operation = values["operation"]
        table_data = create_table(operation)
        # Atualizar a tabela de resultados
        window["result_table"].update(values=table_data)

    # Imprimir a tabela selecionada ao clicar no botão "Treinar" ou "Testar"
    if event == "Treinar Perceptron":
        if values["operation"]:
            print(f"Tabela selecionada: {values['operation']}")
            if values['operation'] == 'AND':
                yResult, wFinal, bFinal = perceptron.andGate()
        else:
            sg.popup("Por favor, selecione uma tabela lógica.")

window.close()
