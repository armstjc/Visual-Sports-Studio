import PySimpleGUI as sg
from vss_utilities import center_window

def vss_about_window(theme='DarkBlue'):
    """
    Generates an 'About VSS' window when this function is called.

    Args:
        None

    Returns:
        None
    """

    sg.theme(theme)
    sg.set_options(
        window_location = (0,0)
        ,element_padding=(5,5)
        #,font = 'Franklin 14'
    )

    layout = [
        
        [sg.Text('About Visual Sports Studio',font='Segoe 20')]
    ]
    window = sg.Window('Visual Sports Stuido',
        layout,
        size=(480,320),
        resizable=True,
        finalize=True
    )
    center_window(window)

    while True: # Event loop
        event, values = window.read()
        
        if event == sg.WIN_CLOSED \
            or event == 'Exit' or str.lower(event) == 'ok':

            break

vss_about_window()