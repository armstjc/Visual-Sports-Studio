import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

def main_window():
    # VARS CONSTS:

    # New figure and plot variables so we can manipulate them

    _VARS = {'window': False,
            'fig_agg': False,
            'pltFig': False}

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg


    # \\  -------- PYSIMPLEGUI -------- //

    AppFont = 'Any 16'
    sg.theme('DarkTeal12')
    seasons = [x for x in range(2010,2020)]
    layout = [[sg.Canvas(key='figCanvas')],
            [sg.Spin(seasons,key='-SPIN_SEA-'),sg.Button('Update', font=AppFont), sg.Button('Exit', font=AppFont)]]
    _VARS['window'] = sg.Window('Such Window',
                                layout,
                                finalize=True,
                                resizable=True,
                                location=(100, 100),
                                element_justification="right")

    # \\  -------- PYSIMPLEGUI -------- //


    # \\  -------- PYPLOT -------- //


    def makeSynthData(season:int):
        url = f'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/teams-{season}.csv'
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

    drawChart(2010)

    # MAIN LOOP
    while True:
        event, values = _VARS['window'].read(timeout=200)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        # New Button (check the layout) and event catcher for the plot update
        if event == 'Update':
            updateChart(int(values['-SPIN_SEA-']))
    _VARS['window'].close()

def main():
    main_window()

if __name__ == '__main__':
    main()