import PySimpleGUI as sg
from vss_defaults import VSS_APPLICATION_VERSIOIN, VSS_APPLICATION_NAME, VSS_APPLICATION_DESCRIPTION
from vss_utils.vss_utilities import center_window

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
        
        [
            sg.Text(
                f'About {VSS_APPLICATION_NAME}',
                justification='center',
                font='Segoe 20',
                expand_x=True
            )
        ],
        [   
            sg.Text(
                f'Version: {VSS_APPLICATION_VERSIOIN}',
                justification='center',
                font='Segoe 12',
                expand_x=True
            )
        ],
        [   
            sg.Text(
                f'Author: Joseph Armstrong',
                justification='center',
                font='Segoe 12',
                expand_x=True
            )
        ],
        [   
            sg.Text(
                VSS_APPLICATION_DESCRIPTION,
                font='Segoe 12',
            )
        ],
        [sg.Push(),sg.Button('OK',key='-OK-',size=(10,1),bind_return_key=True),sg.Push()]
    ]
    window = sg.Window(
        'Visual Sports Stuido',
        layout,
        size=(600,480),
        resizable=False,
        no_titlebar=True,
        finalize=True,
        grab_anywhere=True,
        keep_on_top=True
    )
    center_window(window)

    while True: # Event loop
        event, values = window.read()
        
        if event == sg.WIN_CLOSED \
            or event == 'Exit' or event == '-OK-':

            break


if __name__ == "__main__":
    vss_about_window()