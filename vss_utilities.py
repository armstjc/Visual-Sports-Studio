import os

def center_window(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x,y = (screen_width - win_width)//2, (screen_height - win_height)//2
    window.move(x,y)

def create_temp_dir(temp_dir=''):
    try:
        os.mkdir(temp_dir+'temp')
    except:
        print('Temp directory already exists.')