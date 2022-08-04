import PySimpleGUI as sg

def menu():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Storm Islands Bot')],
                [sg.Text('Waves'), sg.InputText()],
                [sg.Text('Attacks'), sg.InputText()],
                [sg.Button('Start')] ]

    # Create the Window
    window = sg.Window('Goodgame Empire Bot', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Start': # if user closes window or clicks cancel
            break
    return values[0], values[1]

    window.close()