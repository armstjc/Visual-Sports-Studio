############################################################################################################################################
##
##  vss_baseball.py
##------------------------------------------------------------------------------------------------------------------------------------------
##
##  TODO: create description of this file.


import matplotlib.pyplot as plt
import pandas as pd
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from vss_urls import RETROSPLIT_TEAM_BOX, RETROSPLIT_PLAYER_BOX,\
    RETROSPLIT_HEAD_TO_HEAD
from vss_utilities import center_window, vss_error
from vss_utils import vss_baseball_graph_stat_types, \
    vss_baseball_team_stats_col_list, \
    vss_baseball_team_stats_column_swaper, \
    vss_baseball_player_stats_col_list, \
    vss_baseball_player_stats_column_swaper, \
    vss_baseball_head_to_head_column_swaper, \
    vss_baseball_head_to_head_col_list, \
    vss_baseball_batting_by_position_column_swaper, \
    vss_baseball_batting_by_position_col_list


def baseball_main_window(theme='DarkBlue'):
    sg.theme(theme)
    menu_bar = [
        ['File',['---','Exit']],
        ['Settings'],
        ['Help',['About VSS']]
    ]
    _VARS = {'window': False,
            'fig_agg': False,
            'pltFig': False}

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg


    # def makeSynthData(season:int):
    #     url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/teams-{season}.csv'
    #     df = pd.read_csv(url)
    #     xData = df['B_R'].tolist()
    #     yData = df['P_R'].tolist()
    #     return (xData, yData)


    def getData(season:int,url:str,x_col:str,y_col:str):
        #data_url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/teams-{season}.csv'
        try:
            df = pd.read_csv(url)
            xData = df[x_col].tolist()
            yData = df[y_col].tolist()
            return (xData, yData)
        except Exception as e:
            vss_error(e)

    def drawChart(season:int,url:str,x_col:str,y_col:str):
        _VARS['pltFig'] = plt.figure()
        dataXY = getData(season,url,x_col,y_col)
        try:
            plt.plot(dataXY[0], dataXY[1], '.k')
            plt.xlabel('Runs scored')
            plt.ylabel('Runs Allowed')
            plt.title(f'Runs Scored vs Runs Allowed, {season} MLB Season.')
        except:
            ## This is to prevent a scenario where the app calls this function,
            ## without any data to chart.
            plt.plot([1,2,3],[1,2,3], '.k')
            plt.xlabel('click the "Update" button to generate a new chart.')
            plt.ylabel('Once you have restablished your internet connection,')
            plt.title(f'An error occured.\nCheck your internet connection.')
        _VARS['fig_agg'] = draw_figure(
            _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

    def updateChart(season:int,url:str,x_col:str,y_col:str,\
        x_label:str,y_label:str,chart_title=""):
        has_data = True
        _VARS['fig_agg'].get_tk_widget().forget()

        try:
            dataXY = getData(season,url,x_col,y_col)
        except Exception as e:
            vss_error(e)
                
        try:
            plt.clf()
        except:
            print('No chart to clear')
        plt.plot(dataXY[0], dataXY[1], '.k')

        if str.lower(x_label) != str.lower('X-Axis'):
            plt.xlabel(x_label)
        else:
            plt.xlabel(x_label)

        if str.lower(x_label) != str.lower('Y-Axis'):
            plt.ylabel(y_label)
        else:
            plt.ylabel(y_label)
        
        if chart_title != "" and chart_title == str.lower("Title"):
            plt.title(chart_title)
        else:
            plt.title(f'{x_col} vs {y_col}, {season} MLB Season.')
        
        _VARS['fig_agg'] = draw_figure(
            _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

    AppFont = 'Any 12'
    
    stat_seasons = [x for x in range(1901,2021)]
    #stat_types = ['Player Stats','Team Stats']
    stat_types = vss_baseball_graph_stat_types()

    graph_col = sg.Column([[sg.Canvas(key='figCanvas')]])

    stat_col_list = vss_baseball_team_stats_col_list()

    settings_col = sg.Column(
        [
            [
                sg.Frame(
                    "Select a stat category:",
                    layout=[
                        [
                            sg.Combo(
                                #button_text='Select a stat.',
                                values=stat_types,
                                size=(25,1),
                                default_value="Team Stats",
                                enable_events=True,
                                key="-LIST_STAT-"
                            )
                            
                        ]
                    ]
                )
            ],
            [
                sg.Frame(
                    "Select a column for the X axis:",
                    layout=[
                        [
                            sg.Combo(
                                #button_text='Select a stat.',
                                stat_col_list,
                                size=(25,1),
                                default_value="Batting - R",
                                enable_events=True,
                                key='-X_STAT-'
                            )
                            
                        ]
                    ]
                )
            ],
            [
                sg.Frame(
                    'Select a column for the Y axis:',
                    layout=[
                        [
                            sg.Combo(
                                #button_text='Select a stat.',
                                stat_col_list,
                                size=(25,1),
                                default_value="Pitching - R",
                                key='-Y_STAT-'
                            )
                            
                        ]
                    ]
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
                                sg.Frame('X-Axis Title:',
                                    layout=[[
                                        sg.Input(
                                            default_text='X-Axis',
                                            size=(25,1),
                                            key='-CUSTOM_X_TITLE-'
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
                                
                            ]
                    ]
                )
            ],
            [sg.Frame(
                'Select a season:',
                layout=[
                    [
                        sg.Spin(
                            stat_seasons,
                            initial_value=2021,
                            size=(20,1),
                            key='-SPIN_SEA-'
                        ),
                        sg.Button('Update', font=AppFont)
                    ]
                ],
                )
            ],
            [sg.Button('Exit', font=AppFont)]
        ]
    )

    graphing_layout =[
        [settings_col,graph_col]
    ]

    stats_layout = [
        [sg.Text('This is placeholder test.')],
        [sg.Text('In the future, this is a spreadsheet.')]
    ]

    layout = [
        [sg.Menu(menu_bar,visible=True)],
        [sg.TabGroup(
                [
                    [
                        sg.Tab('Graphing', graphing_layout,visible=True),
                        sg.Tab('Stats',stats_layout,visible=False)
                    ]
                ],
                expand_x=True,
                expand_y=True
            
            )
        ]
    ]

    ## Window Declaration. This is  
    _VARS['window'] = sg.Window('Baseball - Visual Sports Stuido',
                                layout,
                                finalize=True,
                                resizable=True,
                                location=(0, 0),
                                element_justification="right")

    # Due to the way this app is designed, a chart has to be made first.
    drawChart(
        2020,
        RETROSPLIT_TEAM_BOX.format(season=2010),
                "B_R",
                "P_R"
    ) 
    center_window(_VARS['window'])
    
    while True: # Event Loop
        event, values = _VARS['window'].read(timeout=200)
        #print(values)
        #print(event)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        ##############################################################################################################################################
        ## User Interface (UI) update
        ##############################################################################################################################################

        if event == '-LIST_STAT-' and values['-LIST_STAT-'] == 'Team Stats':
            stat_col_list = vss_baseball_team_stats_col_list()

            _VARS['window']['-X_STAT-'].update(values=stat_col_list,value="Batting - R")
            _VARS['window']['-Y_STAT-'].update(values=stat_col_list,value="Pitching - R")
            #stat_seasons = [x for x in range(1901,2021)]

            stat_seasons = [x for x in range(1901,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)

        elif event == '-LIST_STAT-'  and  values['-LIST_STAT-'] == 'Player Stats':
            stat_col_list = vss_baseball_player_stats_col_list()

            _VARS['window']['-X_STAT-'].update(values=stat_col_list,value="Batting - R")
            _VARS['window']['-Y_STAT-'].update(values=stat_col_list,value="Pitching - R")

            stat_seasons = [x for x in range(1901,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)

        elif event == '-LIST_STAT-'  and  values['-LIST_STAT-'] == 'Head-to-Head':
            stat_col_list = vss_baseball_head_to_head_col_list()

            _VARS['window']['-X_STAT-'].update(values=stat_col_list,value="Batting - PA")
            _VARS['window']['-Y_STAT-'].update(values=stat_col_list,value="Batting - HR")

            stat_seasons = [x for x in range(1974,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)

        elif event == '-LIST_STAT-'  and  values['-LIST_STAT-'] == 'Batting by Position':
            stat_col_list = vss_baseball_batting_by_position_col_list()

            _VARS['window']['-X_STAT-'].update(values=stat_col_list,value="Batting - PA")
            _VARS['window']['-Y_STAT-'].update(values=stat_col_list,value="Batting - HR")

            stat_seasons = [x for x in range(1974,2021)]
            _VARS['window']['-SPIN_SEA-'].update(values=stat_seasons)

        ##############################################################################################################################################
        ## Graph Update
        ##############################################################################################################################################

        if event == 'Update' and values['-LIST_STAT-'] == 'Team Stats':
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_TEAM_BOX.format(season=int(values['-SPIN_SEA-'])),
                vss_baseball_team_stats_column_swaper(values['-X_STAT-']),
                vss_baseball_team_stats_column_swaper(values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                values['-CUSTOM_TITLE-']
            )
            
        elif event == 'Update' and values['-LIST_STAT-'] == 'Player Stats':
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_PLAYER_BOX.format(season=int(values['-SPIN_SEA-'])),
                vss_baseball_player_stats_column_swaper(values['-X_STAT-']),
                vss_baseball_player_stats_column_swaper(values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                values['-CUSTOM_TITLE-']
            )
            
        elif event == 'Update' and values['-LIST_STAT-'] == 'Head-to-Head':
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_HEAD_TO_HEAD.format(season=int(values['-SPIN_SEA-'])),
                vss_baseball_head_to_head_column_swaper(values['-X_STAT-']),
                vss_baseball_head_to_head_column_swaper(values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                values['-CUSTOM_TITLE-']
            )
            
        elif event == 'Update' and values['-LIST_STAT-'] == 'Batting by Position':
            updateChart(
                int(values['-SPIN_SEA-']),
                RETROSPLIT_HEAD_TO_HEAD.format(season=int(values['-SPIN_SEA-'])),
                vss_baseball_batting_by_position_column_swaper(values['-X_STAT-']),
                vss_baseball_batting_by_position_column_swaper(values['-Y_STAT-']),
                values['-CUSTOM_X_TITLE-'],
                values['-CUSTOM_Y_TITLE-'],
                values['-CUSTOM_TITLE-']
            )


    _VARS['window'].close()


if __name__ == "__main__":
    baseball_main_window()