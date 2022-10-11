############################################################################################################################################
##
##  main.py
##------------------------------------------------------------------------------------------------------------------------------------------
##
##  TODO: create description of this file.
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from numpy.random import rand
import os
import pandas as pd

def make_dpi_aware():
    import ctypes
    import platform
    if int(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_temp_directory():
    try:
        os.rmdir('temp')
    except:
        print('For some reason, the temp directory no longer exits.')

def create_temp_directory():
    try:
        os.mkdir('temp')
    except:
        print('Temp directory already downloaded')

def get_data(season:int):
    schedule_url = 'https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/daybyday/teams-2015.csv'
    season_schedule_df = pd.read_csv(schedule_url,sep=",")
    x = season_schedule_df['B_R'].tolist() # Runs scored
    y = season_schedule_df['P_R'].tolist() # Runs allowed
    return x, y

def load_sample_data():
    df = pd.read_csv('Book1.csv')
    x = df['x'].tolist()
    y = df['y'].tolist()
    return x, y

def main_window():
    seasons = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
    make_dpi_aware()
    sg.set_options(
        window_location = (0,0)
    )

    layout = [
        [sg.Spin(seasons,key='-SPIN_SEA-')],
        [sg.Button('Get Data',key='-DATA_FETCH-'),sg.Canvas(key='-GRAPH-',expand_x=True,pad=(10,10),size=(250,250),background_color='red')],
        [sg.Button('Update'),sg.Button('Exit')]
    ]

    window = sg.Window('Visual Sports Stuido',layout,finalize=True)

    # canvas_elem = window['-GRAPH-']
    # canvas = canvas_elem.TKCanvas

    # fig, ax = plt.subplots()
    # ax.grid(True)
    # fig_agg = draw_figure(canvas,fig)
    # x,y= load_sample_data()

    # ax.scatter(x,y)

    while True: # Event loop
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        
        if event == '-DATA_FETCH-':
            #print('fetching data')
            canvas_elem = window['-GRAPH-']
            canvas = canvas_elem.TKCanvas
            input_value = int(values['-SPIN_SEA-'])
            fig, ax = plt.subplots()
            ax.grid(True)
            fig_agg = draw_figure(canvas,fig)
            x,y= get_data(input_value)

            ax.scatter(x,y)
            fig_agg.draw()
            
    window.close()
    delete_temp_directory()

def main():
    create_temp_directory()
    main_window()

if __name__ == '__main__':
    main()