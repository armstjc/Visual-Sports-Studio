import PySimpleGUI as sg
from vss_utils.vss_utilities import center_window

def soccer_main_window():
    layout = [
        [sg.Text('This sport has not been implemented yet for this app.')],
        [sg.Text('Press the "Exit" button below to close this popup window.')],
        [sg.Push(),sg.Button('Exit'),sg.Push()]
    ]

    window = sg.Window('Window',layout,finalize=True)
    center_window(window)
    while True: # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    window.close()
