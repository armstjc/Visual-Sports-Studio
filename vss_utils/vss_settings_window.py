import sys

sys.path.append('../Visual-Sports-Studio')
import PySimpleGUI as sg

from vss_defaults import VSS_APPLICATION_NAME, PSG_THEME_LIST_RENAMED
from vss_utils.vss_utilities import center_window, psg_theme_name_swapper, \
    get_application_resolution_list, vss_load_settings, vss_save_settings

def vss_theme_test_window(theme='Dark Blue #01'):
    sg.theme(psg_theme_name_swapper(theme))
    sg.set_options(
        window_location = (0,0)
        ,element_padding=(5,5)
        #,font = 'Franklin 14'
    )

    #vss_settings
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
                size=(20,1),
                default_value="This",
                key='-Y_STAT-'
            )
        ],
        [sg.Text('Press the \"OK\" button to exit.')],
        [sg.Button('OK',size=(8,1),key='-OK-')]
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

def vss_settings_window(settings_json:dict,theme='DarkBlue',\
    window_width=480,window_height=480):
    
    def apply_changes_to_settings(temp_settings:dict,current_settings:dict):
        if temp_settings == current_settings:
            pass
        else:
            vss_save_settings(temp_settings)
            

    # If the user makes any changes to their settings, make those
    # changes to a temp dictionary, to prevent the actual app
    # settings from being altered by the user directly, especially
    # if the user doesn't want to commit to any changes.
    settings_json_temp = settings_json

    sg.theme(theme)
    sg.set_options(
        window_location = (0,0)
        ,element_padding=(5,5)
        #,font = 'Franklin 14'
    )

    general_settings_layout =[
        [
            sg.Text(
                'General Settings',
                justification='center',
                font='Segoe 18',
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
                size=(8,1),
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

        ],
        [
            sg.VPush()
        ],
        [
            sg.Button(
                'Reset all settings',
                key='-RESET_BUTTON-',
                font='Segoe 12',
                tooltip='Will be implemented in a future update',
                expand_x=True,
                disabled=True
            )
        ],
        [
            sg.Button(
                'Open Log Window',
                key='-DEV_LOGS_WINDOW-',
                font='Segoe 12',
                tooltip='Will be implemented in a future update',
                expand_x=True,
                disabled=True
            )
        ]
    ]

    custom_database_settings_layout = [
        [
            sg.Frame(
                'Baseball - MLB:',
                layout =[
                    [
                        sg.Text('Update stats on open'),
                        sg.Push(),
                        sg.Radio('Yes',
                            'down_stats_MLB',
                            key='DOWN_STATS_MLB_TRUE',
                            default=False,
                            disabled=True
                        ),
                        sg.Radio('No',
                            'down_stats_MLB',
                            key='DOWN_STATS_MLB_TRUE',
                            default=True,
                            disabled=True
                        )

                    ],
                    [
                        sg.Text('Delete stats on close'),
                        sg.Push(),
                        sg.Radio(
                            'Yes',
                            'del_stats_MLB',
                            key='-DEL_STATS_MLB_TRUE-',
                            default=False,
                            disabled=True
                        ),
                        sg.Radio('No',
                            'del_stats_MLB',
                            key='-DEL_STATS_MLB_FALSE-',
                            default=True,
                            disabled=True
                        )
                    ]
                ],
                expand_x=True
            )
        ]
    ]

    database_settings_layout = [
        [
            sg.Push(),
            sg.Text(
                'Database Settings',
                justification='center',
                font='Segoe 18',
                
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
                size=(8,1),
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
                enable_events=True,
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
                enable_events=True,
                key='-STATS_UPDATE_VAL-',
                disabled=False

            )
        ],
        [
            sg.Frame(
                'Custom Database settings',
                layout=custom_database_settings_layout,
                expand_x=True,
                #disabled=True
            )
        ],
        [
            sg.VPush()
        ]
    ]

    ## Depricated for now. May reimplement later down in the future.

    # general_settings_tab =[
    #     [
    #         sg.Column(
    #             general_settings_layout,
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
        [
            sg.Text(
                'Settings',
                font='Segoe 24 bold',
                expand_x=True,
                justification='center'

            )
        ],
        [sg.TabGroup(
            [[
                sg.Tab(
                    'General', 
                    general_settings_layout,
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
        ],
        [
            sg.Frame(
                '',
                layout=[[
                    sg.Button(
                        'OK',
                        size=(8,1),
                        key='-OK-',
                        disabled=False
                    ),
                    sg.Button(
                        'Cancel',
                        size=(8,1),
                        key='-CANCEL-',
                        disabled=False
                    ),
                    sg.Button(
                        'Apply',
                        size=(8,1),
                        key='-APPLY-',
                        disabled=True
                    ),
                ]],
                element_justification='right',
                expand_x=True
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
        event, values = settings_window.read(timeout=500)
        print(event)
        #print(values)
        if event == sg.WIN_CLOSED or event == 'Exit' or event == '-OK-':
            print('No changes in settings.')
            break
        elif event == '-APPLY-':
            apply_changes_to_settings(settings_json_temp,settings_json)
            settings_json = settings_json_temp
        elif event == '-CANCEL-':
            break

        if event == '-VSS_THEME_TEST-':
            #print(values['-VSS_THEME-'])
            vss_theme_test_window(values['-VSS_THEME-'])

        if settings_json != settings_json_temp:
            settings_window['-APPLY-'].update(disabled=False)
        else:
            settings_window['-APPLY-'].update(disabled=True)

    settings_window.close()

if __name__ == "__main__":
    settings_json = vss_load_settings()
    vss_settings_window(settings_json)
