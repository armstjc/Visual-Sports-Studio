##############################################################################################################################################
##                                                                                                                                          ##
##  vss_defaults.py                                                                                                                         ##
##------------------------------------------------------------------------------------------------------------------------------------------##
##                                                                                                                                          ##
##  Author:         Joseph Armstrong (armstjc@mail.uc.edu)                                                                                  ##
##  Description:    Houses stock defaults for the app. Should a critical part of the app be missing, the resources in this file             ## 
##                  should be used to recreate the critical part(s) that are missing.				            							                      ##
##                                                                                                                                          ##
##############################################################################################################################################
import sys
import pandas as pd
from io import StringIO
sys.path.append('../Visual-Sports-Studio')

APPLICATON_RESOLUTIONS_CSV = StringIO("""
name,width,height,ratio
SVGA,800,600,800 x 600
FWVGA,854,480,854 x 480
qHD,960,540,960 x 540
DVGA,960,640,960 x 640
WSVGA,1024,576,1024 x 576
WSVGA,1024,600,1024 x 600
XGA+,1152,864,1152 x 864
XGA+,1152,900,1152 x 900
WXGA,1280,720,1280 x 720
WXGA,1280,768,1280 x 768
WXGA,1280,800,1280 x 800
SXGA,1280,1024,1280 x 1024
WXGA,1360,768,1360 x 768
SXGA+,1400,1050,1400 x 1050
WXGA+,1440,900,1440 x 900
UXGA,1600,1200,1600 x 1200
WSXGA+,1680,1050,1680 x 1050
FHD,1920,1080,1920 x 1080
WUXGA,1920,1200,1920 x 1200
""")
APPLICATION_RESOLUTIONS_DF = pd.read_csv(APPLICATON_RESOLUTIONS_CSV,sep=',')

DEFAULT_FILE_DESCRIPTOR = """

##############################################################################################################################################
##                                                                                                                                          ##
##  file.py																																	##
##------------------------------------------------------------------------------------------------------------------------------------------##
##                                                                                                                                          ##
##  TODO: create description of this file.
##                                                                                                                                          ##
##############################################################################################################################################

"""

DEFAULT_SETTINGS_JSON = """
{
  "app_settings": {
    "main_window_width": 1280,
    "main_window_height": 720,
    "theme":"DarkBlue"
  },
  "custom_database_dir": "temp",
  "database": {
    "database_type": "sqlite3",
    
    "baseball": {
      "mlb": {
        "update_mlb_on_start": false,
        "delete_mlb_on_close": false,
        "explainer": "Tells the app if it should automatically update Major Leauge Baseball (MLB) data at the start and/or if it should delete said data after the app is closed."
      }
    },
    "football": {
      "nfl": {
        "update_nfl_on_start": false,
        "delete_nfl_on_close": false,
        "explainer": "Tells the app if it should automatically update National Football Leauge (NFL) data at the start and/or if it should delete said data after the app is closed."
      },
      "cfb": {
        "update_cfb_on_start": false,
        "delete_cfb_on_close": false,
        "explainer": "Tells the app if it should automatically update NCAA D1 college football (CFB) data at the start and/or if it should delete said data after the app is closed."
      }
    },
    "basketball": {
      "nba": {
        "update_nba_on_start": false,
        "delete_nba_on_close": false,
        "explainer": "Tells the app if it should automatically update National Basketball Association (NBA) data at the start and/or if it should delete said data after the app is closed."
      },
      "cbb": {
        "update_cbb_on_start": false,
        "delete_cbb_on_close": false,
        "explainer": "Tells the app if it should automatically update NCAA D1 Men's College Basketball (CBB) data at the start and/or if it should delete said data after the app is closed."
      },
      "wnba": {
        "update_wnba_on_start": false,
        "delete_wnba_on_close": false,
        "explainer": "Tells the app if it should automatically update Women's National Basketball Association (WNBA) data at the start and/or if it should delete said data after the app is closed."
      },
      "wbb": {
        "update_wbb_on_start": false,
        "delete_wbb_on_close": false,
        "explainer": "Tells the app if it should automatically update NCAA D1 Women's College Basketball (WCBB) data at the start and/or if it should delete said data after the app is closed."
      }
    },
    "hockey": {
      "nhl": {
        "update_nhl_on_start": false,
        "delete_nhl_on_close": false,
        "explainer": "Tells the app if it should automatically update National Hockey League (NHL) data at the start and/or if it should delete said data after the app is closed."
      },
      "phf": {
        "update_phf_on_start": false,
        "delete_phf_on_close": false,
        "explainer": "Tells the app if it should automatically update Premier Hockey Federation (PHF) data at the start and/or if it should delete said data after the app is closed."
      }
    }
  },

  "environment_settings": {
    "explainer": "Tells the app what resolution the windows should be.",
    "window_height": 720,
    "window_width": 1280
  },

  "startup": {
    "premission_to_startup": true,
    "explainer":"With this string, I hereby give you premission to start up!"
  }
}

"""

## Renamed list from sg.theme_previewer()
PSG_THEME_LIST_RENAMED = [
  'Black', 
  'Blue Mono', 
  'Blue Purple', 
  'Bright Colors', 
  'Brown Blue', 
  'Dark #01', 
  'Dark #02', 
  'Dark Amber', 
  'Dark Black #01', 
  'Dark Black #02', 
  'Dark Blue #01', 
  'Dark Blue #02', 
  'Dark Blue #03', 
  'Dark Blue #04', 
  'Dark Blue #05', 
  'Dark Blue #06', 
  'Dark Blue #07', 
  'Dark Blue #08', 
  'Dark Blue #09', 
  'Dark Blue #10', 
  'Dark Blue #11', 
  'Dark Blue #12', 
  'Dark Blue #13', 
  'Dark Blue #14', 
  'Dark Blue #15', 
  'Dark Blue #16', 
  'Dark Blue #17', 
  'Dark Blue #18', 
  'Dark Brown #01', 
  'Dark Brown #02', 
  'Dark Brown #03', 
  'Dark Brown #04', 
  'Dark Brown #05', 
  'Dark Brown #06', 
  'Dark Brown #07', 
  'Dark Green #01', 
  'Dark Green #02', 
  'Dark Green #03', 
  'Dark Green #04', 
  'Dark Green #05', 
  'Dark Green #06', 
  'Dark Green #07', 
  'Dark Grey #01', 
  'Dark Grey #02', 
  'Dark Grey #03', 
  'Dark Grey #04', 
  'Dark Grey #05', 
  'Dark Grey #06', 
  'Dark Grey #07', 
  'Dark Grey #08', 
  'Dark Purple #01', 
  'Dark Purple #02', 
  'Dark Purple #03', 
  'Dark Purple #04', 
  'Dark Purple #05', 
  'Dark Purple #06', 
  'Dark Purple #07', 
  'Dark Red #01', 
  'Dark Red #02', 
  'Dark Red #03', 
  'Dark Tan Blue', 
  'Dark Teal #01', 
  'Dark Teal #02', 
  'Dark Teal #03', 
  'Dark Teal #04', 
  'Dark Teal #05', 
  'Dark Teal #06', 
  'Dark Teal #07', 
  'Dark Teal #08', 
  'Dark Teal #09', 
  'Dark Teal #10',
  'Dark Teal #11', 
  'Dark Teal #12', 
  'Dark Teal #13', 
  'PySimpleGUI Default #1', 
  'PySimpleGUI Default #2', 
  'PySimpleGUI Default #3', 
  'Green', 
  'Green Mono', 
  'Green Tan', 
  'Hot Dog Stand', 
  'Kayak', 
  'Light Blue #01', 
  'Light Blue #02', 
  'Light Blue #03', 
  'Light Blue #04', 
  'Light Blue #05', 
  'Light Blue #06', 
  'Light Blue #07', 
  'Light Blue #08', 
  'Light Brown #01', 
  'Light Brown #02', 
  'Light Brown #03', 
  'Light Brown #04', 
  'Light Brown #05', 
  'Light Brown #06', 
  'Light Brown #07', 
  'Light Brown #08', 
  'Light Brown #09', 
  'Light Brown #10', 
  'Light Brown #11', 
  'Light Brown #12', 
  'Light Brown #13', 
  'Light Brown #14', 
  'Light Gray', 
  'Light Green #01', 
  'Light Green #02', 
  'Light Green #03', 
  'Light Green #04', 
  'Light Green #05', 
  'Light Green #06', 
  'Light Green #07', 
  'Light Green #08', 
  'Light Green #09', 
  'Light Green #10',
  'Light Green #11',
  'Light Grey #01', 
  'Light Grey #02', 
  'Light Grey #03', 
  'Light Grey #04', 
  'Light Grey #05', 
  'Light Grey #06', 
  'Light Grey #07', 
  'Light Purple', 
  'Light Teal', 
  'Light Yellow', 
  'Material #1', 
  'Material #2', 
  'Neutral Blue', 
  'Purple', 
  'Reddit', 
  'Reds', 
  'Sandy Beach', 
  'System Default #1', 
  'System Default #2', 
  'System Default #3', 
  'Tan', 
  'Tan Blue', 
  'Teal Mono', 
  'Topanga'
]

VSS_APPLICATION_VERSION = "0.2.5"

VSS_APPLICATION_NAME = "Visual Sports Studio (Beta)"

VSS_APPLICATION_DESCRIPTION = """
Visual Sports studio (VSS) is an in-development application suite, intended
to help bridge the technological gap between those that want to work with 
sports statisitcs, and those who can program.

This application uses data from and derrived from the Retrosheet project.
Per their request, the following statement must appear prominently:

The information used here was obtained free of
charge from and is copyrighted by Retrosheet.  Interested
parties may contact Retrosheet at 20 Sunset Rd.,
Newark, DE 19711.

Additional special thanks to the people behind SportsDataverse project.
"""

VSS_SUPPORTED_GRAPHS = ['plot','scatter']
