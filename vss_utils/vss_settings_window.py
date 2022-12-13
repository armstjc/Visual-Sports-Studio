import sys
import json
from copy import deepcopy

sys.path.append('../Visual-Sports-Studio')
import PySimpleGUI as sg

from vss_defaults import VSS_APPLICATION_NAME, PSG_THEME_LIST_RENAMED
from vss_utils.vss_utilities import center_window, psg_theme_name_swapper, \
    psg_theme_name_swapper_reverse, get_application_resolution_list, \
    vss_load_settings, vss_save_settings

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
    
    # def apply_changes_to_settings(temp_settings:dict,current_settings:dict):
    #     if temp_settings == current_settings:
    #         pass
    #     else:
    #         vss_save_settings(temp_settings)
            

    # If the user makes any changes to their settings, make those
    # changes to a temp dictionary, to prevent the actual app
    # settings from being altered by the user directly, especially
    # if the user doesn't want to commit to any changes.
    #settings_json = sorted(settings_json.items())
    settings_json_temp = deepcopy(settings_json)

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
                default_value=psg_theme_name_swapper_reverse(settings_json['app_settings']['theme']),
                enable_events=True,
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
                key='-VSS_RES-',
                enable_events=True,
                disabled=False
            ),
               
        ],
        [

        ],
        [
            sg.VPush()
        ],
        [
            sg.Button(
                'Reset all Settings',
                key='-RESET_BUTTON-',
                font='Segoe 12',
                tooltip='Resets all settings changes to the state they were '+
                    '\nprior to opening the settings window.',
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
                            key='-DOWN_STATS_MLB_TRUE-',
                            enable_events=True,
                            default=False,
                            disabled=False
                        ),
                        sg.Radio('No',
                            'down_stats_MLB',
                            key='-DOWN_STATS_MLB_FALSE-',
                            enable_events=True,
                            default=True,
                            disabled=False
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
                key='-STATS_UPDATE_LEVEL-',
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

    settings_changed = False
    theme_settings_changed = False
    resolution_settings_changed = False
    ##############################################################################################################################################
    ## Event Loop
    ##############################################################################################################################################

    while True: 
        event, values = settings_window.read(timeout=500)
        print(event)
        #print(values)


        if event == '-VSS_THEME-':
            settings_json_temp['app_settings']['theme'] = psg_theme_name_swapper(values['-VSS_THEME-'])
            print(settings_json['app_settings']['theme'],settings_json_temp['app_settings']['theme'])
            if settings_json['app_settings']['theme'] != settings_json_temp['app_settings']['theme']:
                theme_settings_changed = True
            else:
                theme_settings_changed = False

        if event == '-VSS_RES-':
            settings_json_temp['app_settings']['main_window_width'] = int(values['-VSS_RES-'].split(' x ',1)[0])
            settings_json_temp['app_settings']['main_window_height'] = int(values['-VSS_RES-'].split(' x ',1)[1])
            
            print(settings_json_temp['app_settings']['main_window_width'],settings_json['app_settings']['main_window_width'])
            print(values['-VSS_RES-'].split(' x ',1))

            if settings_json['app_settings']['main_window_width'] != \
                settings_json_temp['app_settings']['main_window_width'] or \
                settings_json['app_settings']['main_window_height'] != \
                settings_json_temp['app_settings']['main_window_height']:
                resolution_settings_changed = True
            else:
                resolution_settings_changed = False

        if resolution_settings_changed == False and theme_settings_changed == False:
            settings_changed = False
        else:
            settings_changed = True

        # If a user wants to see what a theme looks like before making it their
        # theme for this app, they can click on a test window by clicking the
        # "Try it out" button next to the drop down menu for the current list of themes.
        if event == '-VSS_THEME_TEST-':
            #print(values['-VSS_THEME-'])
            vss_theme_test_window(values['-VSS_THEME-'])
            settings_window['-APPLY-'].update(disabled=False)

        # If the user changes their minds about any settings changes, 
        # but doesn't want to close the settings window,
        # they can hit the "Reset all Settings" button to reset the settings
        # to the way they were before opening the settings window.
        if event == '-RESET_BUTTON-':
            print('Unsaved settings changes have been reversed.')
            settings_window['-VSS_THEME-'].update(value=psg_theme_name_swapper_reverse(settings_json['app_settings']['theme']))
            settings_window['-VSS_RES-'].update(value=f"{settings_json['app_settings']['main_window_width']} x {settings_json['app_settings']['main_window_height']}")

            settings_window['-RESET_BUTTON-'].update(disabled=True)
            settings_json_temp = deepcopy(settings_json)
            
            theme_settings_changed = False
            resolution_settings_changed = False
            settings_changed = False

        if event == '-CANCEL-':
            break
        elif (event == sg.WIN_CLOSED or event == 'Exit' \
            or event == '-OK-' or event == '-APPLY-') \
            and settings_changed == True:
            #sg.popup_yes_no('Are you sure you want to save?')
            #print('No changes in settings.')
            vss_save_settings(settings_json_temp)
            print('Change(s) in settings have been saved.')
            break
        elif (event == sg.WIN_CLOSED or event == 'Exit' \
            or event == '-OK-' or event == '-APPLY-') \
            and settings_changed == False:
            print('No changes in settings.')
            break
                

        if settings_changed == True:
            settings_window['-RESET_BUTTON-'].update(disabled=False)
            settings_window['-APPLY-'].update(disabled=False)
            print('changed')
        else:
            settings_window['-APPLY-'].update(disabled=True)
            print('same')

    settings_window.close()

if __name__ == "__main__":
    settings_json = vss_load_settings()
    vss_settings_window(settings_json)
