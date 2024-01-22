import PySimpleGUI as sg


def creat_window(theme):
    sg.theme(theme)
    layout = [[sg.Text(f'This is example of "{theme}" theme')],
              [sg.InputText()],
              [sg.Button("Close example")],
              [sg.Text(f'    Theme - "{theme}"', font= "Arial 20")]]
    window = sg.Window("Example", layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Close example":
        window.close()

themes = sg.theme_list()

layout = [
    [sg.Table(values=[[str(i)]+[(themes[i-1])] for i in range(1, len(themes))],
              headings=["Number", "Theme"], auto_size_columns=True,
              justification="center", num_rows=min(25, len(themes)),
              key="-TABLE-", enable_events=True)],
    [sg.Button("Exit", size=15)]
]

window = sg.Window("Table of Themes", layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "-TABLE-":
        window.hide()
        creat_window(themes[values["-TABLE-"][0]])
        window.un_hide()

window.close()