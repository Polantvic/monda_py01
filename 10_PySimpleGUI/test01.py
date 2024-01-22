import PySimpleGUI as sg

def creat_window(theme):
    sg.theme(theme)
    sg.popup(theme, font = "Arial 25")
    layout = [[sg.Text("Hello!")],
              [sg.InputText()],
              [sg.Button("BB!"), sg.Button("Next Theme")],
              [sg.Text(f"    Theme - {theme}", font= "Arial 20")]]
    window = sg.Window("Hello, hello!", layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "BB!":
        window.close()
        return False
    elif event == "Next Theme":
        window.close()
        return True


themes = sg.theme_list()
theme_num = 0

while theme_num <= len(themes):
    if creat_window(themes[theme_num]):
        theme_num += 1
    else:
        break
