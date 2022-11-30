import os
import json
import shutil
import sys
import pandas as pd
import platform

sys.path.append('../Visual-Sports-Studio')
import PySimpleGUI as sg
from vss_defaults import DEFAULT_SETTINGS_JSON, APPLICATION_RESOLUTIONS_DF

def get_application_resolution_list(max_res_width=1920,max_res_height=1200):
    res_df = APPLICATION_RESOLUTIONS_DF
    res_df = res_df.loc[res_df['height'] <= max_res_height]
    res_df = res_df.loc[res_df['width'] <= max_res_width]
    
    return res_df['ratio'].to_list()

def center_window(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x,y = (screen_width - win_width)//2, (screen_height - win_height)//2
    window.move(x,y)

def clear_temp_dir():
    file_path = get_user_home_dir()
    file_path = f'{file_path}/visual_sports_studio/temp/'
    file_path = reformat_folder_string(file_path)

    try:
        shutil.rmtree(file_path,ignore_errors=True)
    except Exception as e:
        print('Something went wrong when deleting the temp directory.')
        print('Exception details:\n\n{e}')

def create_dir(c_dir:str):
    try:
        os.mkdir(c_dir)
        print('Directory successfully created.')
    except:
        print('Directory already exists.')

def create_temp_dir():
    file_path = get_user_home_dir()

    file_path = f'{file_path}/visual_sports_studio/'
    file_path = reformat_folder_string(file_path)
    
    print(f'Attempting to create the {file_path} directory.')
    create_dir(file_path)

    file_path = f'{file_path}/temp/'
    file_path = reformat_folder_string(file_path)
    
    print(f'Attempting to create the {file_path} directory.')
    create_dir(file_path)
    
    print('Temp directory successfully created.\n')


def download_chart_data(url:str,x_col:str,y_col:str):
    try:
        df = pd.read_csv(url)
        data_df = pd.DataFrame(df.groupby(x_col,as_index=False)[y_col].value_counts())
        data_df.columns = ['X','Y','count']

        return data_df
    
    except Exception as e:
        vss_error(e)

def get_filetype_in_folder(folder:str,filetype:str):
    files = []
    
    dir_list = os.listdir(folder)
    all_files = list(filter(lambda x: f'.{filetype}' in x, dir_list))
    
    for i in all_files:
        files.append(f'{folder}/{i}')
    
    del all_files
    
    return files

## Returns the platform.uname() class that contains info
## about the OS that is running this app.
def get_os_information():
    return platform.uname()

## If we just need a specific part of the OS information,
## these functions just hands over the information as is.
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

def get_user_home_dir():
    home_dir =  os.path.expanduser( '~' )
    return reformat_folder_string(home_dir)
    
def reformat_folder_string(folder:str):
    folder_dir = folder.replace("\\","/")
    if folder_dir[-1] != '/':
        folder_dir = folder_dir + '/'
    del folder
    folder_dir = folder_dir.replace("//","/")
    return folder_dir

def psg_theme_name_swapper(theme:str):
    match theme:
        # Black
        case "Black":
            return "Black"
        # BlueMono
        case "Blue Mono":
            return "BlueMono"
        # BluePurple
        case "Blue Purple":
            return "BluePurple"
        #BrightColors
        case "Bright Colors":
            return "BrightColors"
        # BrownBlue
        case "Brown Blue":
            return "BrownBlue"
        # Dark
        case "Dark #01":
            return "Dark"
        case "Dark #02":
            return "Dark2"
        # DarkAmber
        case "Dark Amber":
            return "DarkAmber"
        # DarkBlack
        case "Dark Black #01":
            return "DarkBlack"
        case "Dark Black #02":
            return "DarkBlack1"
        # DarkBlue
        case "Dark Blue #01":
            return "DarkBlue"
        case "Dark Blue #02":
            return "DarkBlue1"
        case "Dark Blue #03":
            return "DarkBlue2"
        case "Dark Blue #04":
            return "DarkBlue3"
        case "Dark Blue #05":
            return "DarkBlue4"
        case "Dark Blue #06":
            return "DarkBlue5"
        case "Dark Blue #07":
            return "DarkBlue6"
        case "Dark Blue #08":
            return "DarkBlue7"
        case "Dark Blue #09":
            return "DarkBlue8"
        case "Dark Blue #10":
            return "DarkBlue9"
        case "Dark Blue #11":
            return "DarkBlue10"
        case "Dark Blue #12":
            return "DarkBlue11"
        case "Dark Blue #13":
            return "DarkBlue12"
        case "Dark Blue #14":
            return "DarkBlue13"
        case "Dark Blue #15":
            return "DarkBlue14"
        case "Dark Blue #16":
            return "DarkBlue15"
        case "Dark Blue #17":
            return "DarkBlue16"
        case "Dark Blue #18":
            return "DarkBlue17"
        # DarkBrown
        case "Dark Brown #01":
            return "DarkBrown"
        case "Dark Brown #02":
            return "DarkBrown1"
        case "Dark Brown #03":
            return "DarkBrown2"
        case "Dark Brown #04":
            return "DarkBrown3"
        case "Dark Brown #05":
            return "DarkBrown4"
        case "Dark Brown #06":
            return "DarkBrown5"
        case "Dark Brown #07":
            return "DarkBrown6"
        # DarkGreen
        case "Dark Green #01":
            return "DarkGreen"
        case "Dark Green #02":
            return "DarkGreen1"
        case "Dark Green #03":
            return "DarkGreen2"
        case "Dark Green #04":
            return "DarkGreen3"
        case "Dark Green #05":
            return "DarkGreen4"
        case "Dark Green #06":
            return "DarkGreen5"
        case "Dark Green #07":
            return "DarkGreen6"
        # DarkGrey
        case "Dark Grey #01":
            return "DarkGrey"
        case "Dark Grey #02":
            return "DarkGrey1"
        case "Dark Grey #03":
            return "DarkGrey2"
        case "Dark Grey #04":
            return "DarkGrey3"
        case "Dark Grey #05":
            return "DarkGrey4"
        case "Dark Grey #06":
            return "DarkGrey5"
        case "Dark Grey #07":
            return "DarkGrey6"
        case "Dark Grey #08":
            return "DarkGrey7"
        # DarkPurple
        case "Dark Purple #01":
            return "DarkPurple"
        case "Dark Purple #02":
            return "DarkPurple1"
        case "Dark Purple #03":
            return "DarkPurple2"
        case "Dark Purple #04":
            return "DarkPurple3"
        case "Dark Purple #05":
            return "DarkPurple4"
        case "Dark Purple #06":
            return "DarkPurple5"
        case "Dark Purple #07":
            return "DarkPurple6"
        # DarkRed
        case "Dark Red #01":
            return "DarkRed"
        case "Dark Red #02":
            return "DarkRed1"
        case "Dark Red #03":
            return "DarkRed2"
        # DarkTanBlue
        case "Dark Tan Blue":
            return "DarkTanBlue"
        # DarkTeal
        case "Dark Teal #01":
            return "DarkTeal"
        case "Dark Teal #02":
            return "DarkTeal1"
        case "Dark Teal #03":
            return "DarkTeal2"
        case "Dark Teal #04":
            return "DarkTeal3"
        case "Dark Teal #05":
            return "DarkTeal4"
        case "Dark Teal #06":
            return "DarkTeal5"
        case "Dark Teal #07":
            return "DarkTeal6"
        case "Dark Teal #08":
            return "DarkTeal7"
        case "Dark Teal #09":
            return "DarkTeal8"
        case "Dark Teal #10":
            return "DarkTeal9"
        case "Dark Teal #11":
            return "DarkTeal10"
        case "Dark Teal #12":
            return "DarkTeal11"
        case "Dark Teal #13":
            return "DarkTeal12"
        # Default
        case "PySimpleGUI Default #1":
            return "Default"
        case "PySimpleGUI Default #2":
            return "Default1"
        # DefaultNoMoreNagging
        case "PySimpleGUI Default #3":
            return "DefaultNoMoreNagging"
        # Green
        case "Green":
            return "Green"
        # Green
        case "Green Mono":
            return "GreenMono"
        # Green
        case "Green Tan":
            return "GreenTan"
        # HotDogStand
        case "Hot Dog Stand":
            "HotDogStand"
        # Kayak
        case "Kayak":
            "Kayak"
        # LightBlue
        case "Light Blue #01":
            return "LightBlue"
        case "Light Blue #02":
            return "LightBlue1"
        case "Light Blue #03":
            return "LightBlue2"
        case "Light Blue #04":
            return "LightBlue3"
        case "Light Blue #05":
            return "LightBlue4"
        case "Light Blue #06":
            return "LightBlue5"
        case "Light Blue #07":
            return "LightBlue6"
        case "Light Blue #08":
            return "LightBlue7"
        # LightBrown
        case "Light Brown #01":
            return "LightBrown"
        case "Light Brown #02":
            return "LightBrown1"
        case "Light Brown #03":
            return "LightBrown2"
        case "Light Brown #04":
            return "LightBrown3"
        case "Light Brown #05":
            return "LightBrown4"
        case "Light Brown #06":
            return "LightBrown5"
        case "Light Brown #07":
            return "LightBrown6"
        case "Light Brown #08":
            return "LightBrown7"
        case "Light Brown #09":
            return "LightBrown8"
        case "Light Brown #10":
            return "LightBrown9"
        case "Light Brown #11":
            return "LightBrown10"
        case "Light Brown #12":
            return "LightBrown11"
        case "Light Brown #13":
            return "LightBrown12"
        case "Light Brown #14":
            return "LightBrown13"
        # LightGreen
        case "Light Gray":
            return "LightGray1"
        # LightGreen
        case "Light Green #01":
            return "LightGreen"
        case "Light Green #02":
            return "LightGreen1"
        case "Light Green #03":
            return "LightGreen2"
        case "Light Green #04":
            return "LightGreen3"
        case "Light Green #05":
            return "LightGreen4"
        case "Light Green #06":
            return "LightGreen5"
        case "Light Green #07":
            return "LightGreen6"
        case "Light Green #08":
            return "LightGreen7"
        case "Light Green #09":
            return "LightGreen8"
        case "Light Green #10":
            return "LightGreen9"
        case "Light Green #11":
            return "LightGreen10"
        # LightGrey
        case "Light Grey #01":
            return "LightGrey"
        case "Light Grey #02":
            return "LightGrey1"
        case "Light Grey #03":
            return "LightGrey2"
        case "Light Grey #04":
            return "LightGrey3"
        case "Light Grey #05":
            return "LightGrey4"
        case "Light Grey #06":
            return "LightGrey5"
        case "Light Grey #07":
            return "LightGrey6"
        # LightPurple
        case "Light Purple":
            return "LightPurple"
        # LightTeal
        case "Light Teal":
            return "LightTeal"
        # LightYellow
        case "Light Yellow":
            return "LightYellow"
        # Material1
        case "Material #1":
            return "Material1"
        case "Material #2":
            return "Material2"
        # NeutralBlue
        case "Neutral Blue":
            return "NeutralBlue"
        # Purple
        case "Purple":
            return "Purple"
        # Reddit
        case "Reddit":
            return "Reddit"
        # Reds
        case "Reds":
            return "Reds"
        # SandyBeach
        case "Sandy Beach":
            return "SandyBeach"
        # SystemDefault
        case "System Default #1":
            return "SystemDefault"
        case "System Default #2":
            return "SystemDefault1"
        case "System Default #3":
            return "SystemDefaultForReal"
        # Tan
        case "Tan":
            return "Tan"
        # TanBlue
        case "Tan Blue":
            return "TanBlue"
        # TealMono
        case "Teal Mono":
            return "TealMono"
        # Topanga
        case "Topanga":
            return "Topanga"
        case _:
            # This should not happen, but it will raise an 
            # error to prevent memory shenanagans.
            raise Exception("Not a supported column.")

def vss_error(exception_description:str):
    sg.popup_error(
        f"The following exception has occured with this app:\n{exception_description}",
        title=f"An error occurred with this application.",
        modal=True,
        keep_on_top=True,
        grab_anywhere=True)

def vss_load_settings():

    file_path = get_user_home_dir()
    file_path = f'{file_path}/visual_sports_studio/'
    file_path = reformat_folder_string(file_path)
    create_dir(file_path)

    print(f'File path: {file_path}')

    try:
        with open(f'{file_path}settings.json','r+') as f:
            settings_json_str = f.read()
        print('File loaded.') 
        print('Attempting to verify that the file loaded is a valid JSON file.')

    except:
        print('No settings.json file found. Creating a settings file.')
        settings_json_str = DEFAULT_SETTINGS_JSON
        with open(f'{file_path}settings.json','w+') as f:
            f.write(settings_json_str)
        print('Settings file created!\n')

    try:
        settings_json = json.loads(settings_json_str)
        print("Success! File verified as a JSON file.")
    except ValueError as err:
        print(f"INVALID JSON DECTED!\nReason:\n{err}")
        print('Rewriting settings file')
        settings_json_str = DEFAULT_SETTINGS_JSON
        settings_json = json.loads(settings_json_str)
        with open(f'{file_path}settings.json','w+') as f:
            f.write(str(settings_json))
        print('Settings file created!\n')

    if settings_json['startup']['explainer'] == \
        "With this string, I hereby give you premission to start up!"\
        and settings_json['startup']['premission_to_startup'] == True:

        print('Settings file has correct header.')
        print('The JSON file is in fact the settings JSON file for Visual Sports Studio.')

    else:
        print('INVALID JSON DETECTED!!\n'+
            'The JSON file loaded is not intended to be used as '+
            'the settings JSON for this app.')
        print('Rewriting settings file')
        settings_json_str = DEFAULT_SETTINGS_JSON
        settings_json = json.loads(settings_json_str)
        with open(f'{file_path}settings.json','w+') as f:
            f.write(str(settings_json))
        print('Settings file created!\n')

    del settings_json_str
    return settings_json
    
def vss_save_settings(settings_json:dict):
    # In case the pseudo AppData folder got deleted,
    # this code recreates that directory.
    file_path = get_user_home_dir()
    file_path = f'{file_path}/visual_sports_studio/'
    file_path = reformat_folder_string(file_path)
    create_dir(file_path)

    print(f'File path: {file_path}')

    with open(f'{file_path}settings.json','w+') as f:
        f.write(settings_json)
    print('Settings file saved.')
    print('All Done!\n')

    
if __name__ == "__main__":
    #print(get_application_resolution_list())
    #print(get_user_home_dir())
    create_temp_dir()
    vss_load_settings()