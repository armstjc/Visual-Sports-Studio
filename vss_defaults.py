##############################################################################################################################################
##                                                                                                                                          ##
##  vss_defaults.py                                                                                                                         ##
##------------------------------------------------------------------------------------------------------------------------------------------##
##                                                                                                                                          ##
##  Author:         Joseph Armstrong (armstjc@mail.uc.edu)                                                                                  ##
##  Description:    Houses stock defaults for the app. Should a critical part of the app be missing, the resources in this file             ## 
##                  should be used to recreate the critical part(s) that are missing.				            							##
##                                                                                                                                          ##
##############################################################################################################################################

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
    "main_window_height": 720
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
    "explainer":"Placeholder for functions in the future."
  }
}

"""


VSS_APPLICATION_VERSIOIN = "0.2.0"

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
