import PySimpleGUI as sg

def menu():
    sg.theme('DarkAmber')   # Add a touch of color
    choices = ('attack', 'mark')
    # All the stuff inside your window.
    layout = [  [sg.Text('Storm Islands Bot')],
                [sg.Text('Which bot do you wanna use?')],
                [sg.Radio('Desert', 'bot', key='desert'), sg.Radio('Peak', 'bot', key='peak'), sg.Radio('Storm Islands', 'bot', key='islands'), sg.Radio('Beri', 'bot', key='beri'), sg.Radio('Peak and Desert', 'bot', key='peak_desert')],
                [sg.Text('Waves'), sg.InputText(default_text='0')],
                [sg.Text('Attacks'), sg.InputText(default_text='0')],
                [sg.Text('Desert distance'), sg.InputText(default_text='0')],
                [sg.Text('Peaks distance'), sg.InputText(default_text='0')],
                [sg.Text('Islands distance'), sg.InputText(default_text='0')],
                [sg.Radio('Whole Map', 'whole_map', key='wholemap')],
                [sg.Text('Attack or mark?')],
                [sg.Listbox(choices, size=(15, len(choices)), key='type', enable_events=True, default_values='mark')],
                [sg.Button('Start')] ]

    # Create the Window
    window = sg.Window('Goodgame Empire Bot', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Start': # if user closes window or clicks cancel
            break
    return values[0], values[1], values['type'][0], values['desert'], values['peak'], values['islands'], values['beri'], values['peak_desert'], values[2], values[3], values[4], values['wholemap']

    window.close()