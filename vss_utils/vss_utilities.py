import os
import json
import shutil
import sys
import pandas as pd
import platform

sys.path.append('../Visual-Sports-Studio')
import PySimpleGUI as sg
from vss_defaults import DEFAULT_SETTINGS_JSON

def center_window(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x,y = (screen_width - win_width)//2, (screen_height - win_height)//2
    window.move(x,y)

def clear_temp_dir(temp_dir=''):
    try:
        shutil.rmtree(temp_dir+'temp',ignore_errors=True)
    except:
        print('Directory already exists.')

def create_temp_dir(temp_dir=''):
    try:
        os.mkdir(temp_dir+'temp')
    except:
        print('Temp directory already exists.')

def download_chart_data(url:str,x_col:str,y_col:str):
    try:
        df = pd.read_csv(url)
        data_df = pd.DataFrame(df.groupby(x_col,as_index=False)[y_col].value_counts())
        data_df.columns = ['X','Y','count']

        return data_df
    
    except Exception as e:
        vss_error(e)

def vss_error(exception_description:str):
    sg.popup_error(
                f"The following exception has occured with this app:\n{exception_description}",
                title=f"An error occurred with this application.",
                modal=True,
                keep_on_top=True,
                grab_anywhere=True)

def vss_load_settings():
    try:
        with open('settings.json','r+') as f:
            settings_json = f.read()
        print('File loaded. Attempting to verify that the file loaded is a valid JSON file.')

    except:
        print('No settings.json file found. Creating a settings file.')
        settings_json = DEFAULT_SETTINGS_JSON
        with open('settings.json','w+') as f:
            f.write(settings_json)
        print('Settings file created')

    try:
        json.loads(settings_json)
        print("Success!")
    except ValueError as err:
        print(f"INVALID JSON DECTED!\nReason:\n{err}")


def get_os_type():
    return platform.uname().system

def get_machine_name():
    return platform.uname().node

def get_os_release():
    return platform.uname().release

def get_os_version():
    return platform.uname().version

def get_machine_type():
    return platform.uname().machine


print(get_os_type())