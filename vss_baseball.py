############################################################################################################################################
##
##  vss_baseball.py
##------------------------------------------------------------------------------------------------------------------------------------------
##
##  TODO: create description of this file.


import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from vss_utilities import center_window



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


    def makeSynthData(season:int):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/teams-{season}.csv'
        df = pd.read_csv(url)
        xData = df['B_R'].tolist()
        yData = df['P_R'].tolist()
        return (xData, yData)

    def getData(season:int,x_col:str,y_col:str,url:str):
        #data_url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/teams-{season}.csv'
        df = pd.read_csv(url)
        xData = df['B_R'].tolist()
        yData = df['P_R'].tolist()
        return (xData, yData)


    def drawChart(season:int):
        _VARS['pltFig'] = plt.figure()
        dataXY = makeSynthData(season)
        plt.plot(dataXY[0], dataXY[1], '.k')
        _VARS['fig_agg'] = draw_figure(
            _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

    def updateChart(season:int):
        _VARS['fig_agg'].get_tk_widget().forget()
        dataXY = makeSynthData(season)
        # plt.cla()
        plt.clf()
        plt.plot(dataXY[0], dataXY[1], '.k')
        _VARS['fig_agg'] = draw_figure(
            _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

    AppFont = 'Any 12'
    
    stat_seasons = [x for x in range(1901,2021)]
    stat_types = ['Player Stats','Team Stats']
    # stat_types = [
    #     'Player Stats',
    #     'Team Stats',
    #     'Head to Head',
    #     'Batting by Position',
    #     'Batting By Runners',
    #     'Batting by Platoon (L/R vs. L/R)',
    #     'Pitching by Position',
    #     'Pitching By Runners',
    #     'Pitching by Platoon (L/R vs. L/R)'
    # ]

    graph_col = sg.Column([[sg.Canvas(key='figCanvas')]])
    settings_col = sg.Column(
        [
            [
                sg.Frame(
                    'Select a stat category:',
                    layout=[
                        [
                            sg.OptionMenu(
                                #button_text='Select a stat.',
                                stat_types,
                                
                                key='-LIST_STAT-'
                            )
                            
                        ]
                    ]
                )
            ],
            [
                sg.Frame(
                    'Select a column for the X axis:',
                    layout=[
                        [
                            sg.OptionMenu(
                                #button_text='Select a stat.',
                                stat_types,
                                
                                key='-LIST_STAT-'
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
                            sg.OptionMenu(
                                #button_text='Select a stat.',
                                stat_types,
                                
                                key='-LIST_STAT-'
                            )
                            
                        ]
                    ]
                )
            ],
            [
                sg.Frame(
                    'Select a season:',
                    layout=[
                        [
                            sg.Spin(stat_seasons,key='-SPIN_SEA-'),
                            sg.Button('Update', font=AppFont)
                        ]
                    ]
                )
            ],
            [
                sg.Button('Exit', font=AppFont)
            ]
        ]
    )

    layout = [
        [sg.Menu(menu_bar,visible=True)],
        [settings_col,graph_col]
    ]
            
    _VARS['window'] = sg.Window('Such Window',
                                layout,
                                finalize=True,
                                resizable=True,
                                location=(0, 0),
                                element_justification="right")

    
    drawChart(2010) # Due to the way this is designed, a chart has to be made first.
    center_window(_VARS['window'])
    # MAIN LOOP
    while True:
        event, values = _VARS['window'].read(timeout=200)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        # New Button (check the layout) and event catcher for the plot update
        if event == 'Update':
            updateChart(int(values['-SPIN_SEA-']))
    _VARS['window'].close()