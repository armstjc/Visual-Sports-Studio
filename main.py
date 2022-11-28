##############################################################################################################################################
##                                                                                                                                          ##
##  main.py                                                                                                                                 ##
##------------------------------------------------------------------------------------------------------------------------------------------##
##                                                                                                                                          ##
##  TODO: create description of this file.
##                                                                                                                                          ##
##############################################################################################################################################

## Required to start.
import PySimpleGUI as sg
import sys


sys.path.append('../Visual-Sports-Studio')
## Imports neede to load in individual Sport windows
from vss_sports.vss_baseball import baseball_main_window
from vss_sports.vss_basketball import basketball_main_window
from vss_sports.vss_football import football_main_window
from vss_sports.vss_soccer import soccer_main_window
from vss_utils.vss_utilities import center_window, create_temp_dir, clear_temp_dir
from vss_defaults import VSS_APPLICATION_NAME

def main_window(theme='DarkBlue'):
    #BTN_SIZE = (5,5)
    sg.theme(theme)
    sg.set_options(
        window_location = (0,0)
        ,element_padding=(5,5)
        #,font = 'Franklin 14'
    )

    menu_bar = [
        ['File',['---','Exit']],
        ['Settings'],
        ['Help',['About VSS']]
    ]

    

    body_layout = [
        
        [
            sg.Text(
                f'Welcome to {VSS_APPLICATION_NAME}',
                font='Segoe 20',
                expand_x=True
            ),
            sg.Button(image_filename='icons/settings.png',
                tooltip='Settings',
                visible=True)
        ],
        [sg.Text('Select a sport to get started.')],
        #sg.Push(),
        [
            sg.Button(#'Baseball',
                image_filename='icons/baseball_50x50.png',
                tooltip='Baseball',
                visible=True,
                disabled=False,
                auto_size_button=False,
                # size=BTN_SIZE,
                # expand_x=True,
                # expand_y=True,
                key='-BASEBALL-'
            ),
            sg.Text('Baseball',size=(15,1),font='Segoe 14'),
            sg.Text('MLB baseball data')
        ],
        #sg.Push(),
        [sg.Text('Comming soon, but shown here for demonstrative purposes.',justification='center',font='italic 10')],
        [
            sg.Button(#'American Football',
                image_filename='icons/football_50x50.png',
                tooltip='American Football',
                visible=True,
                disabled=False,
                auto_size_button=False,
                # size=BTN_SIZE,
                # expand_x=True,
                # expand_y=True,
                key='-FOOTBALL-'
            ),
            sg.Text('American Football',size=(15,1),font='Segoe 14',tooltip='Also known as \"American Football\", \"Gridiron Football\", or \"Football\".'),
            sg.Text('NFL football data.')
        ],
        [
            sg.Button(#'Soccer',
                image_filename='icons/soccer_50x50.png',
                tooltip='Association Football (Soccer)',
                visible=True,
                disabled=False,
                auto_size_button=False,
                # size=BTN_SIZE,
                # expand_x=True,
                # expand_y=True,
                key='-SOCCER-'
            ),
            sg.Text('Soccer',size=(15,1),font='Segoe 14',tooltip='Also known as \"Association Football\", \"Soccer\", or \"Football\".'),
            sg.Text('Soccer data from around the world.')
        ],
        [
            sg.Button(#'Basketball',
                image_filename='icons/basketball_50x50.png',
                tooltip='Basketball',
                visible=True,
                disabled=False,
                auto_size_button=False,
                # size=BTN_SIZE,
                # expand_x=True,
                # expand_y=True,
                key='-BASKETBALL-'
            ),
            sg.Text('Basketball',size=(15,1),font='Segoe 14',tooltip='Basketball'),
            sg.Text('Basketball data from around the world.')
        ],
    ]


    layout = [
        #[sg.Titlebar('Welcome to Visual Sports Studio')],
        [sg.Menu(menu_bar,visible=True)],
        [
            #sg.Column(sidebar_layout),
            #sg.VSeparator(),
            sg.Column(
                body_layout,
                expand_x=True,
            )
        ]
    ]
    window = sg.Window(f'{VSS_APPLICATION_NAME}',
        layout,
        default_button_element_size=(100,20),
        #resizable=True,
        finalize=True
    )
    
    center_window(window)
    create_temp_dir()
    while True: # Event loop
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            #clear_temp_dir()
            break
        
        if event == '-BASKETBALL-':
            basketball_main_window()

        if event == '-BASEBALL-':
            baseball_main_window()

        if event == '-FOOTBALL-':
            football_main_window()

        if event == '-SOCCER-':
            soccer_main_window()
            
    window.close()

def main():
    
    main_window()

if __name__ == '__main__':
    main()