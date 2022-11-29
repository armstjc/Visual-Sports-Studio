############################################################################################################################################
##
##  vss_baseball.py
##------------------------------------------------------------------------------------------------------------------------------------------
##
##  TODO: create description of this file.

import sys
import matplotlib.pyplot as plt

import threading

sys.path.append('../Visual-Sports-Studio')
import PySimpleGUI as sg
from vss_db.vss_db_baseball import sqlite3_baseball_multithreading
from vss_defaults import VSS_APPLICATION_NAME, VSS_SUPPORTED_GRAPHS
from vss_utils.vss_urls import RETROSPLIT_TEAM_BOX, RETROSPLIT_PLAYER_BOX,\
    RETROSPLIT_HEAD_TO_HEAD, RETROSPLIT_BATTIN_BY_POSITION, \
    RETROSPLIT_BATTING_BY_RUNNERS, RETROSPLIT_BATTING_BY_PLATOON, \
    RETROSPLIT_PITCHING_BY_RUNNERS    
from vss_utils import vss_baseball_batting_by_platoon_column_swaper, \
    vss_baseball_batting_by_platoon_col_list, \
    vss_baseball_batting_by_position_col_list, \
    vss_baseball_batting_by_position_column_swaper, \
    vss_baseball_batting_by_runners_column_swaper, \
    vss_baseball_batting_by_runners_col_list, \
    vss_baseball_graph_stat_types, \
    vss_baseball_head_to_head_column_swaper, \
    vss_baseball_head_to_head_col_list, \
    vss_baseball_pitching_by_platoon_column_swaper, \
    vss_baseball_pitching_by_platoon_col_list,\
    vss_baseball_pitching_by_runners_column_swaper, \
    vss_baseball_pitching_by_runners_col_list, \
    vss_baseball_player_stats_col_list, \
    vss_baseball_player_stats_column_swaper, \
    vss_baseball_reverse_column_swaper,\
    vss_baseball_team_stats_col_list, \
    vss_baseball_team_stats_column_swaper
from vss_utils.vss_graphing import draw_figure
from vss_utils.vss_utilities import center_window, download_chart_data, \
    vss_error
    

def baseball_main_window(theme='DarkBlue', \
    window_width=1280,window_height=720):
    sg.theme(theme)
    menu_bar = [
        ['File',['Main Menu','---','Exit']],
        ['Settings',['App Settings']],
        ['Help',['About VSS']]
    ]
    _VARS = {'window': False,
            'fig_agg': False,
            'pltFig': False}


    def drawChart(season:int,url:str,x_col:str,y_col:str):
        _VARS['pltFig'] = plt.figure()

        dataXY = download_chart_data(url,x_col,y_col)

        try:
            plt.scatter(dataXY['X'], dataXY['Y'])
            plt.xlabel('Runs scored')
            plt.ylabel('Runs Allowed')
            plt.title(f'Runs Scored vs Runs Allowed, {season} MLB Season.')
            plt.grid()
        except:
            ## This is to prevent a scenario where 
            ## the app calls this function,
            ## but without any data to chart.
            plt.plot([1,2,3],[1,2,3], '.k')
            plt.xlabel(
                'click the "Update" button to generate a new chart.')
            plt.ylabel(
                'Once you have restablished your internet connection,')
            plt.title(
                f'An error occured.\nCheck your internet connection.')

        _VARS['fig_agg'] = draw_figure(
            _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

    def updateChart(season:int,url:str,x_col:str,y_col:str,\
        x_label:str,y_label:str,plot_type='plot',chart_title="",\
        gridlines=True):
        has_data = True
        _VARS['fig_agg'].get_tk_widget().forget()

        try:
            dataXY = download_chart_data(url,x_col,y_col)
            try:
                plt.clf()
            except:
                print('No chart to clear')

            if plot_type in VSS_SUPPORTED_GRAPHS:
                if plot_type == 'plot':
                    #plt.plot(dataXY[0], dataXY[1], '.k')
                    #print(max(dataXY[0]))
                    plt.plot(dataXY['X'], dataXY['Y'], '.k')
                elif plot_type == 'scatter':
                    plt.scatter(dataXY['X'], dataXY['Y'],s=dataXY['count'])
                else:
                    raise Exception('Unsuported chart type.')
            else:
                raise Exception('Unsuported chart type.')


            if x_label != 'X-Axis':
                plt.xlabel(x_label)
            else:
                plt.xlabel(vss_baseball_reverse_column_swaper(x_col))

            if y_label != 'Y-Axis':
                plt.ylabel(y_label)
            else:
                plt.ylabel(vss_baseball_reverse_column_swaper(y_col))
            
            if chart_title != "" and chart_title == str.lower("Title"):
                plt.title(chart_title)
            else:
                plt.title(f'{vss_baseball_reverse_column_swaper(x_col)}'+ \
                    f' vs {vss_baseball_reverse_column_swaper(y_col)},'+ \
                    f' {season} MLB Season.')
            
            if gridlines == True:
                plt.grid()

            _VARS['fig_agg'] = draw_figure(
                _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

        except Exception as e:
            vss_error(e)
                

    AppFont = 'Any 12'

    ##############################################################################################################################################
    ## Graphing section of VSS Baseball
    ##############################################################################################################################################

    stat_seasons = [x for x in range(1901,2021)]
    stat_types = vss_baseball_graph_stat_types()

    graph_col = sg.Column(
        [[
            sg.Canvas(
                key='figCanvas',
                expand_x=True,
                expand_y=True
            )
        ]],
        expand_x=True,
        expand_y=True
    )

    stat_col_list = vss_baseball_team_stats_col_list()

    graph_settings_col = sg.Column(
        [
            [
                sg.Frame(
                    "Select a stat category:",
                    layout=[[
                        sg.Combo(
                            #button_text='Select a stat.',
                            values=stat_types,
                            size=(30,1),
                            default_value="Team Stats",
                            enable_events=True,
                            key="-LIST_STAT-"
                        )
                    ]]
                )
            ],
            [
                sg.Frame(
                    'Select a column for the Y axis:',
                    layout=[[
                        sg.Combo(
                            #button_text='Select a stat.',
                            stat_col_list,
                            size=(30,1),
                            default_value="Pitching - Runs allowed (R)",
                            key='-Y_STAT-'
                        )
                    ]]
                )
            ],
            [
                sg.Frame(
                    "Select a column for the X axis:",
                    layout=[[
                        sg.Combo(
                            #button_text='Select a stat.',
                            stat_col_list,
                            size=(30,1),
                            default_value="Batting - Runs Scored (R)",
                            enable_events=True,
                            key='-X_STAT-'
                        )
                    ]]
                )
            ],
            [
                sg.Frame(
                    'Table Customization:',
                    layout=[
                        [
                        sg.Frame('Title:',
                            layout=[[
                                sg.Input(
                                    default_text='Title',
                                    size=(25,1),
                                    key='-CUSTOM_TITLE-'
                                )
                            ]]
                        )
                    ],
                    [
                        sg.Frame('Y-Axis Title:',
                            layout=[[
                                sg.Input(
                                    default_text='Y-Axis',
                                    size=(25,1),
                                    key='-CUSTOM_Y_TITLE-'
                                )
                            ]]
                        )                        
                    ],
                    [
                        sg.Frame('X-Axis Title:',
                            layout=[[
                                sg.Input(
                                    default_text='X-Axis',
                                    size=(25,1),
                                    key='-CUSTOM_X_TITLE-'
                                )
                            ]]
                        )                            
                    ]]
                )
            ],
            [sg.Frame(
                'Select a season:',
                layout=[[
                        sg.Spin(
                            stat_seasons,
                            initial_value=2021,
                            size=(20,1),
                            key='-SPIN_SEA-'
                        ),
                        sg.Button('Update', font=AppFont)
                    ]],
                )
            ],
            [sg.Button('Exit', font=AppFont)]
        ],
        # scrollable=True,
        # vertical_scroll_only=True,
        # expand_y=True
    )

    graphing_layout =[[
        graph_settings_col,
        graph_col    
    ]]
    
    ##############################################################################################################################################
    ## Stats section of VSS Baseball
    ##############################################################################################################################################

    stats_layout = [
        [sg.Text('This is placeholder test.')],
        [sg.Text('In the future, this is a spreadsheet.')]
    ]
    
    ##############################################################################################################################################
    ## Layout of VSS Baseball
    ##############################################################################################################################################

    layout = [
        [sg.Menu(menu_bar,visible=True)],
        [sg.TabGroup(
            [[
                sg.Tab('Graphing', graphing_layout,visible=True),
                sg.Tab('Stats',stats_layout,visible=False)
            ]],
            expand_x=True,
            expand_y=True
            
            )
        ]
    ]
    
    ##############################################################################################################################################
    ## Window declaration of VSS Baseball
    ##############################################################################################################################################

    ## Window Declaration. This is  
    _VARS['window'] = sg.Window(f'Baseball - {VSS_APPLICATION_NAME}',
        layout,
        finalize=True,
        resizable=True,
        location=(0, 0),
        size=(window_width,window_height),
        element_justification="right")

    # Due to the way this app is designed, a chart has to be made first.
    drawChart(
        2020,
        RETROSPLIT_TEAM_BOX.format(season=2020),
        "B_R",
        "P_R"
    ) 
    center_window(_VARS['window'])
    
    #threading.Thread(target=sqlite3_baseball_multithreading, daemon=True).start()
    
    ##############################################################################################################################################
    ## Event Loop
    ##############################################################################################################################################

    while True: 
        event, values = _VARS['window'].read(timeout=200)
        # print(values)
        # print(event)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        
        
        ##############################################################################################################################################
        ## User Interface (UI) update
        ##############################################################################################################################################

        if event == '-LIST_STAT-' and \
        values['-LIST_STAT-'] == 'Team Stats':
            stat_col_list = vss_baseball_team_stats_col_list()

            _VARS['window']['-X_STAT-'].update(
                values=stat_col_list,value="Batting - Runs Scored (R)")
            _VARS['window']['-Y_STAT-'].update(
                values=stat_col_list,value="Pitching - Runs allowed (R)")
            #stat_seasons = [x for x in range(1901,2021)]

            stat_seasons = [x for x in range(1901,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)

        elif event == '-LIST_STAT-' and \
        values['-LIST_STAT-'] == 'Player Stats':
            stat_col_list = vss_baseball_player_stats_col_list()

            _VARS['window']['-X_STAT-'].update(
                values=stat_col_list,value="Batting - Runs Scored (R)")
            _VARS['window']['-Y_STAT-'].update(
                values=stat_col_list,value="Pitching - Runs allowed (R)")

            stat_seasons = [x for x in range(1901,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)

        elif event == '-LIST_STAT-' and \
        values['-LIST_STAT-'] == 'Head-to-Head':
            stat_col_list = vss_baseball_head_to_head_col_list()

            _VARS['window']['-X_STAT-'].update(
                values=stat_col_list,value="Batting - Plate Appearances (PA)")
            _VARS['window']['-Y_STAT-'].update(
                values=stat_col_list,value="Batting - Home Runs (HR)")

            stat_seasons = [x for x in range(1974,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)

        elif event == '-LIST_STAT-' and \
        values['-LIST_STAT-'] == 'Batting by Position':
            stat_col_list = vss_baseball_batting_by_position_col_list()

            _VARS['window']['-X_STAT-'].update(
                values=stat_col_list,value="Batting - Plate Appearances (PA)")
            _VARS['window']['-Y_STAT-'].update(
                values=stat_col_list,value="Batting - Home Runs (HR)")

            stat_seasons = [x for x in range(1974,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)

        elif event == '-LIST_STAT-' and \
        values['-LIST_STAT-'] == 'Batting by Runners':
            stat_col_list = vss_baseball_batting_by_runners_col_list()

            _VARS['window']['-X_STAT-'].update(
                values=stat_col_list,value="Batting - Plate Appearances (PA)")
            _VARS['window']['-Y_STAT-'].update(
                values=stat_col_list,value="Batting - Home Runs (HR)")

            stat_seasons = [x for x in range(1974,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)

        elif event == '-LIST_STAT-' and \
        values['-LIST_STAT-'] == 'Batting by Platoon (L/R vs. L/R)':
            stat_col_list = vss_baseball_batting_by_platoon_col_list()

            _VARS['window']['-X_STAT-'].update(
                values=stat_col_list,value="Batting - Plate Appearances (PA)")
            _VARS['window']['-Y_STAT-'].update(
                values=stat_col_list,value="Batting - Home Runs (HR)")

            stat_seasons = [x for x in range(1974,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)

        elif event == '-LIST_STAT-' and \
        values['-LIST_STAT-'] == 'Pitching by Runners':
            stat_col_list = vss_baseball_pitching_by_runners_col_list()

            _VARS['window']['-X_STAT-'].update(
                values=stat_col_list,value="Pitching - Plate Appearances (PA)")
            _VARS['window']['-Y_STAT-'].update(
                values=stat_col_list,value="Pitching - Home Runs allowed (HR)")


            stat_seasons = [x for x in range(1974,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)

        elif event == '-LIST_STAT-' and \
        values['-LIST_STAT-'] == 'Pitching by Platoon (L/R vs. L/R)':
            stat_col_list = vss_baseball_pitching_by_platoon_col_list()

            _VARS['window']['-X_STAT-'].update(
                values=stat_col_list,value="Pitching - Plate Appearances (PA)")
            _VARS['window']['-Y_STAT-'].update(
                values=stat_col_list,value="Pitching - Home Runs allowed (HR)")

            stat_seasons = [x for x in range(1974,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)




        ##############################################################################################################################################
        ## Graph Update
        ##############################################################################################################################################

        if event == 'Update' and \
        values['-LIST_STAT-'] == 'Team Stats':
            
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_TEAM_BOX.format(
                    season=int(values['-SPIN_SEA-'])),
                vss_baseball_team_stats_column_swaper(
                    values['-X_STAT-']),
                vss_baseball_team_stats_column_swaper(
                    values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                'scatter',
                values['-CUSTOM_TITLE-']
            )
            
        elif event == 'Update' and \
        values['-LIST_STAT-'] == 'Player Stats':
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_PLAYER_BOX.format(
                    season=int(values['-SPIN_SEA-'])),
                vss_baseball_player_stats_column_swaper(
                    values['-X_STAT-']),
                vss_baseball_player_stats_column_swaper(
                    values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                'scatter',

                values['-CUSTOM_TITLE-']
            )
            
        elif event == 'Update' and \
        values['-LIST_STAT-'] == 'Head-to-Head':
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_HEAD_TO_HEAD.format(
                    season=int(values['-SPIN_SEA-'])),
                vss_baseball_head_to_head_column_swaper(
                    values['-X_STAT-']),
                vss_baseball_head_to_head_column_swaper(
                    values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                'scatter',
                values['-CUSTOM_TITLE-']
            )
            
        elif event == 'Update' and \
        values['-LIST_STAT-'] == 'Batting by Position':
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_BATTIN_BY_POSITION.format(
                    season=int(values['-SPIN_SEA-'])),
                vss_baseball_batting_by_position_column_swaper(
                    values['-X_STAT-']),
                vss_baseball_batting_by_position_column_swaper(
                    values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                'scatter',
                values['-CUSTOM_TITLE-']
            )
            
        elif event == 'Update' and \
        values['-LIST_STAT-'] == 'Batting by Runners':
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_BATTING_BY_RUNNERS.format(
                    season=int(values['-SPIN_SEA-'])),
                vss_baseball_batting_by_runners_column_swaper(
                    values['-X_STAT-']),
                vss_baseball_batting_by_runners_column_swaper(
                    values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                'scatter',
                values['-CUSTOM_TITLE-'],

            )
            
        elif event == 'Update' and \
        values['-LIST_STAT-'] == 'Batting by Platoon (L/R vs. L/R)':
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_BATTING_BY_PLATOON.format(
                    season=int(values['-SPIN_SEA-'])),
                vss_baseball_batting_by_platoon_column_swaper(
                    values['-X_STAT-']),
                vss_baseball_batting_by_platoon_column_swaper(
                    values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                'scatter',
                values['-CUSTOM_TITLE-']
            )
            
        elif event == 'Update' and \
        values['-LIST_STAT-'] == 'Pitching by Runners':
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_PITCHING_BY_RUNNERS.format(
                    season=int(values['-SPIN_SEA-'])),
                vss_baseball_pitching_by_runners_column_swaper(
                    values['-X_STAT-']),
                vss_baseball_pitching_by_runners_column_swaper(
                    values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                'scatter',
                values['-CUSTOM_TITLE-']
            )
            
        elif event == 'Update' and \
        values['-LIST_STAT-'] == 'Pitching by Platoon (L/R vs. L/R)':
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_PITCHING_BY_RUNNERS.format(
                    season=int(values['-SPIN_SEA-'])),
                vss_baseball_pitching_by_platoon_column_swaper(
                    values['-X_STAT-']),
                vss_baseball_pitching_by_platoon_column_swaper(
                    values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                'scatter',
                values['-CUSTOM_TITLE-']
            )

    _VARS['window'].close()

##############################################################################################################################################
## If this script is run "as-is", the following code opens up the 
## VSS Baseball window anyways:
##############################################################################################################################################

if __name__ == "__main__":
    #baseball_main_window("DarkBlue",800,600)
    baseball_main_window()