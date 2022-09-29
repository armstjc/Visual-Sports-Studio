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

DEFAULT_SETTINGS_JSON = {"database": {
    ## DBMS Settings
    "database_type":"sqlite3", ## Likely won't be a thing for this capstone project, but in the future, I plan on supporting other DBMS engines.
    
    ## Startup

    ### Baseball
    "update_mlb_on_start":False, ## Tells the app if it should automatically update Major Leauge Baseball (MLB) data at the start.
    ### American Football
    "update_nfl_on_start":False, ## Tells the app if it should automatically update National Football Leauge (NFL) data at the start.
    "update_cfb_on_start":False, ## Tells the app if it should automatically update NCAA D1 college football (CFB) data at the start.
    ### Men's Basketball
    "update_nba_on_start":False, ## Tells the app if it should automatically update National Basketball Association (NBA) data at the start.
    "update_cbb_on_start":False, ## Tells the app if it should automatically update NCAA D1 Men's College Basketball (CBB) data at the start.
    ### Women's Basketball
    "update_wnba_on_start":False, ## Tells the app if it should automatically update Women's National Basketball Association (WNBA) data at the start.
    "update_wbb_on_start":False, ## Tells the app if it should automatically update NCAA D1 Women's College Basketball (CBB) data at the start.
    ### Men's Hockey
    "update_nhl_on_start":False, ## Tells the app if it should automatically update National Hockey League (NHL) data at the start.
    ### Women's Hockey
    "update_phf_on_start":False, ## Tells the app if it should automatically update Premier Hockey Federation (PHF) data at the start.

    ## File I/O
    "custom_database_dir":"", ## If specified by the user, this is the directory they want the SQL databases in.

    ## Close

    ### Baseball
    "delete_mlb_on_close":False, ## Tells the app if it should automatically delete the Major Leauge Baseball (MLB) data when the app is closed.
    ### American Football
    "delete_nfl_on_close":False, ## Tells the app if it should automatically delete the National Football Leauge (NFL) data when the app is closed.
    "delete_cfb_on_close":False, ## Tells the app if it should automatically delete the NCAA D1 college football (CFB) data when the app is closed.
    ### Men's Basketball
    "delete_nba_on_close":False, ## Tells the app if it should automatically delete National Basketball Association (NBA) data when the app is closed.
    "delete_cbb_on_close":False, ## Tells the app if it should automatically delete NCAA D1 Men's College Basketball (CBB) data when the app is closed.
    ### Women's Basketball
    "delete_wnba_on_close":False, ## Tells the app if it should automatically delete Women's National Basketball Association (WNBA) data when the app is closed.
    "delete_wbb_on_close":False, ## Tells the app if it should automatically delete NCAA D1 Women's College Basketball (CBB) data when the app is closed.
    ### Men's Hockey
    "delete_nhl_on_close":False, ## Tells the app if it should automatically delete National Hockey League (NHL) data when the app is closed.
    ### Women's Hockey
    "delete_phf_on_close":False, ## Tells the app if it should automatically delete Premier Hockey Federation (PHF) data when the app is closed.
},
"app_settings":{
    ## This is 720p
    "main_window_width":1280,
    "main_window_height":720,
}}


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