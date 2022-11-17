import os
import shutil

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