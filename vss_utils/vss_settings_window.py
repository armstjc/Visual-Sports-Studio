import sys

sys.path.append('../Visual-Sports-Studio')
import PySimpleGUI as sg

from vss_defaults import VSS_APPLICATION_NAME, PSG_THEME_LIST_RENAMED
from vss_utils.vss_utilities import center_window, psg_theme_name_swapper, get_application_resolution_list

def vss_theme_test_window(theme='Dark Blue #01'):
    sg.theme(psg_theme_name_swapper(theme))
    sg.set_options(
        window_location = (0,0)
        ,element_padding=(5,5)
        #,font = 'Franklin 14'
    )

    layout = [
        [
            sg.Text(
                f"""
This is a test of the application theme "{theme}",
internally called "{psg_theme_name_swapper(theme)}" by PySimpleGUI, 
the GUI backend of this application.
                """.strip()
            )
        ],
        [
            sg.Text(
                'This is a button. \n'+
                'This button specifically does nothing special.'
            )
        ],
        [
            sg.Button('Button')
        ],
        [
            sg.Text('This is a combo List.\n'+
                'It has no use or purpose here.'
            )
        ],
        [
            sg.Combo(
                
                ['This','Is','A','Combo','List.',
                    'It','Has','No','Use','Or','Purpose','Here'],
                size=(30,1),
                default_value="This",
                key='-Y_STAT-'
            )
        ],
        [sg.Text('Press the \"OK\" button to exit.')],
        [sg.Button('OK',size=(10,1),key='-OK-')]
    ]

    test_window = sg.Window(
        'Test Window',
        layout,
        finalize=True,
        resizable=False,
        keep_on_top=True,
        location=(0, 0),
        size=(360,320),
        element_justification="center"

    )

    #center_window(test_window)
    #test_window.move_to_center()
    while True: # Event Loop
        event, values = test_window.read()
        if event == sg.WIN_CLOSED or event == 'Exit' or event == '-OK-':
            break

    test_window.close()

def vss_settings_window(theme='DarkBlue',\
    window_width=480,window_height=480):
    
    sg.theme(theme)
    sg.set_options(
        window_location = (0,0)
        ,element_padding=(5,5)
        #,font = 'Franklin 14'
    )

    visual_settings_layout =[
        [
            sg.Text(
                'Visual Settings',
                justification='center',
                font='Segoe 20',
                expand_x=True
            )
        ],
        [
            sg.Text(
                'Visual theme:\t',
                tooltip='Determines the color/visual theme of Visual Sports Studio.\n'+
                    'By default, the theme is set to \"Dark Blue #01\".',
                font='Segoe 12'
            ),
            sg.Push(),
            sg.Button(
                'Try it out',
                tooltip='If you want to see this theme in action, \n'+
                    'click this button to generate a preview window that \nshows how '+
                    'this theme will look in Visual Sports Studio.',
                size=(10,1),
                font='Segoe 12',
                key='-VSS_THEME_TEST-'
            ),
            sg.Combo(
                PSG_THEME_LIST_RENAMED,
                size=(20,1),
                tooltip='Click this list to see a list of built-in '+
                    'application themes supported by Visual Sports Studio.\n'+
                    'By default, the theme is set to \"Dark Blue #01\".',
                default_value='Dark Blue #01',
                key='-VSS_THEME-'
            )
            
        ],
        [
            sg.Text('Window resolution:',font='Segoe 12'),
            sg.Push(),
            sg.Combo(
                get_application_resolution_list(),
                size=(20,1),
                default_value='1280 x 720',
                key='-VSS_RES-'
            ),
               
        ],
        [
            sg.Text('Temp directory:\t',font='Segoe 12'),
            sg.Push(),
            sg.FolderBrowse(size=(10,1),font='Segoe 12',key='-F_BROWSE-'),
            sg.Input(size=(22,1),key='-TEMP_DIR-')

        ]
    ]

    
    database_settings_layout = [
        [
            sg.Push(),
            sg.Text(
                'Database Settings',
                justification='center',
                font='Segoe 20',
                
                expand_x=True
            ),
            sg.Push()
        ],
        [
            sg.Text(
                'Database type:\t',
                tooltip='Database engine used by this isntance of Visual Sports Studio'+
                    '\nIf you\'re not versed in databases, or with ODBC connections, '+
                    'leave this as \"sqlite3\".',
                font='Segoe 12'),
            sg.Push(),
            sg.Button(
                'Advanced',
                size=(10,1),
                tooltip='Advanced settings for the database used by '+
                    'this instance of Visual Sports Studio.',
                key='-ADV_DB-',
                disabled=True
            ),
            sg.Combo(
                ['sqlite3'], # Will be expanded on when DB functionality is expanded.
                size=(20,1),
                tooltip='Database engine used by this isntance of Visual Sports Studio'+
                    '\nIf you\'re not versed in databases, or with ODBC connections, '+
                    'leave this as \"sqlite3\".',
                default_value='sqlite3',
                key='-DB_TYPE-',
                disabled=True
            )
        ],
        [
            sg.Text(
                'Data Update settings:\t',
                font='Segoe 12'
            ),
            sg.Push(),
            sg.Combo(
                ['Update All','Update None','Custom'],
                size=(20,1),
                tooltip='',
                default_value='Update None',
                key='-STATS_UPDATE_VAL-',
                disabled=False

            )
        ],
        [
            sg.Frame(
                'Custom Database settings',
                layout=[
                    [
                        
                    ]
                ]
            )
        ]
    ]

    ## Depricated for now. May reimplement later down in the future.

    # visual_settings_tab =[
    #     [
    #         sg.Column(
    #             visual_settings_layout,
    #             scrollable=True,
    #             vertical_scroll_only=True,
    #             expand_x=True,
    #             expand_y=True
    #         )
    #     ]
    # ]

    # database_settings_tab = [
    #     [
    #         sg.Column(
    #             database_settings_layout,
    #             scrollable=True,
    #             vertical_scroll_only=True,
    #             expand_x=True,
    #             expand_y=True
    #         )
    #     ]
    # ]

    layout = [
        [sg.TabGroup(
            [[
                sg.Tab(
                    'Visual', 
                    visual_settings_layout,
                    visible=True
                ),
                sg.Tab('Database',
                    database_settings_layout,
                    visible=True
                )
            ]],
            expand_x=True,
            expand_y=True
            
            )
        ]
    ]

    settings_window = sg.Window(
        f'Settings - {VSS_APPLICATION_NAME}',
        layout,
        finalize=True,
        resizable=True,
        location=(0, 0),
        size=(window_width,window_height),
        element_justification="right"
    )

    #settings_window.move_to_center()
    center_window(settings_window)
    #settings_window.move(120,120)

    while True: # Event Loop
        event, values = settings_window.read()

        print(values)
        if event == sg.WIN_CLOSED or event == 'Exit' or event == '-OK-':
            break
        
        if event == '-VSS_THEME_TEST-':
            #print(values['-VSS_THEME-'])
            vss_theme_test_window(values['-VSS_THEME-'])

    settings_window.close()

if __name__ == "__main__":
    vss_settings_window()
    #vss_theme_test_window()