##############################################################################################################################################
##                                                                                                                                          ##
##  vss_db_baseball.py																														##
##------------------------------------------------------------------------------------------------------------------------------------------##
##                                                                                                                                          ##
##  Author: 		Joseph Armstrong (armstjc@mail.uc.edu)																					##
##	Description:	Houses functions for VSS to use to create or update database tables that are used by the app.                           ##
##                                                                                                                                          ##
##############################################################################################################################################

import sqlite3
import threading
from datetime import datetime
import pandas as pd
import sys


sys.path.append('../Visual-Sports-Studio')
from vss_db.vss_db_tables import SQLITE_MLB_CHADWICK_PEOPLE_TABLE, \
    SQLITE_MLB_RETROSHEET_SCHEDULE_TABLE, \
    SQLITE_MLB_RETROSHEET_PEOPLE_TABLE, \
    SQLITE_MLB_RETROSHEET_BALLPARK_TABLE, \
    SQLITE_MLB_RETROSHEET_EJECTIONS_TABLE, \
    SQLITE_MLB_RETROSHEET_FRANCHISE_TABLE, \
    SQLITE_MLB_STATCAST_PBP_TABLE, SQLITE_MLB_RETROSPLITS_PLAYER_BOX, \
    SQLITE_VACUUM_COMMAND
import vss_utils.vss_urls as vss_urls 

from multiprocessing import Process
import time

def sqlite3_baseball_multithreading(db_dir="temp"):
    """
    Using the power of multitheading, sqlite3_baseball() downloads
    data publicly advalible from the Retrosheet project,
    and inserts the downloaded data into the SQLite3 instance that 
    Visual Sports Studio uses when run.

    Args:
        db_dir (str):
            Used to determine the temp directory the app/user wants to 
            save data to.

    Returns:
        None
    """
    start_time = datetime.now()

    # Puts the functions in a position to be multi-threaded
    p1 = threading.Thread(target= sqlite3_chadwick_people(db_dir))
    p2 = threading.Thread(target= sqlite3_retrosheet_schedules(db_dir))
    p3 = threading.Thread(target= sqlite3_retrosheet_ballparks(db_dir))
    p4 = threading.Thread(target= sqlite3_retrosheet_ejections(db_dir))
    p5 = threading.Thread(target= sqlite3_retrosheet_franchises(db_dir))
    #p6 = threading.Thread(target= sqlite3_statcast_Pbp(2022)) ## This takes way too long. It needs to be it's own function call.

    # Starts up the functions that are ready to be multi-threaded
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    #p6.start()
    

    # Tells Python to wait for the multi-threaded functions to be done.
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    #p6.join()

    # sqlite3_retrosheet_people()
    # sqlite3_retrosheet_schedules()
    # sqlite3_retrosheet_ballparks()
    # sqlite3_retrosheet_ejections()
    # sqlite3_retrosheet_franchises()
    #sqlite3_statcast_Pbp(2022)
    end_time = datetime.now()
    run_time = end_time-start_time
    print(f'{datetime.now()}\tRetrosheet Data successfuly downloaded.')
    print(f'Took {run_time} to do these actions.')
    return run_time

def sqlite3_baseball_multiprocessing(db_dir="temp"):
    """
    Using the power of multiprocessing, sqlite3_baseball() downloads
    data publicly advalible from the Retrosheet project,
    and inserts the downloaded data into the SQLite3 instance that 
    Visual Sports Studio uses when run.

    Args:
        db_dir (str):
            Used to determine the temp directory the app/user wants to 
            save data to.

    Returns:
        None
    """

    start_time = datetime.now()

    # Puts the functions in a position to be multi-threaded
    p1 = Process(target= sqlite3_chadwick_people(db_dir))
    p2 = Process(target= sqlite3_retrosheet_schedules(db_dir))
    p3 = Process(target= sqlite3_retrosheet_ballparks(db_dir))
    p4 = Process(target= sqlite3_retrosheet_ejections(db_dir))
    p5 = Process(target= sqlite3_retrosheet_franchises(db_dir))

    # Starts up the functions that are ready to be multi-threaded
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    

    # Tells Python to wait for the multi-threaded functions to be done.
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    
    # sqlite3_retrosheet_people()
    # sqlite3_retrosheet_schedules()
    # sqlite3_retrosheet_ballparks()
    # sqlite3_retrosheet_ejections()
    # sqlite3_retrosheet_franchises()
    #sqlite3_statcast_Pbp(2022)
    end_time = datetime.now()
    run_time = end_time-start_time
    print(f'{datetime.now()}\tRetrosheet Data successfuly downloaded.')
    print(f'Took {run_time} to do these actions.')
    return run_time

############################################################################################################################################
##
##  Retrosheet functions
##------------------------------------------------------------------------------------------------------------------------------------------
##
##      Functions that take data from the Retrosheet baseball project,
##      and puts the resulting data in a SQLite database that a user running
##      Visual Sports Studio can use, and an advanced user can copy/export/use
##      the data with ease.
##
############################################################################################################################################

def sqlite3_chadwick_people(db_dir="temp"):
    """
    When called, this function downloads the Chadwick People spreadsheet
    to the local SQLite database that is created for this application at 
    launch, or recreates the datbase if it doesn't exist when this 
    function is called.

    Args:
        db_dir (str):
            Used to determine the temp directory the app/user wants to 
            save data to.

    Returns:
        None
    """
    
    con = sqlite3.connect(f"{db_dir}/vss_baseball.sqlite",check_same_thread=True)
    cur = con.cursor()

    ## Delete the existing table if it exists...     
    print(f'{datetime.now()}\tAttempting to create the [mlb_chadwick_people] table.')
    cur.execute("DROP TABLE IF EXISTS mlb_chadwick_people;")
    
    ## ..and then create the table (see vss_db_tables.py for the code behind the table).
    cur.execute(SQLITE_MLB_CHADWICK_PEOPLE_TABLE)
    print(f'{datetime.now()}\t[mlb_chadwick_people] has been created.')

    print(f'{datetime.now()}\tAttempting to download the Chadwick people data.')
    chadwick_people_df = pd.read_csv(vss_urls.CHADWICK_PEOPLE,sep=",",)
    
    print(f'{datetime.now()}\tSuccessfully downloaded the Chadwick people data. Moving to insert the Chadwick people data into the SQLite3 database.')
    
    chadwick_people_df.to_sql("mlb_chadwick_people",con,if_exists="append",index=False)

    ## This is done to prevent memory leaks. We don't need this data anymore, so we are deleting these variables to free up memory.
    del chadwick_people_df
    print(f'{datetime.now()}\tSuccessfully inserted the Chadwick people data into the SQLite3 database.')

    
    con.close()

def sqlite3_retrosheet_ballparks(db_dir="temp"):
    """
    Retrives the current Retrosheet ballparks text file,
    converts the file into a Pandas dataframe (read: spreadsheet), 
    and then sends the dataframe to the VSS SQLite3 database.

    Call this fuction only if you want to nuke the existing data. 
    If this function is called, pre-existing data will be deleted!

    Args:
        None

    Returns:
        None
    """
    ## Connect to the SQLite instance for Visual Sports Studio (vss_baseball.sqlite).
    con = sqlite3.connect(f"{db_dir}/vss_baseball_retrosheet.sqlite",check_same_thread=True) ## TODO: Make a universal filename for the SQLite instance.
    
    cur = con.cursor()
    
    ## Delete the existing table if it exists... 
    print(f'{datetime.now()}\tAttempting to create the [mlb_retrosheet_ballparks] table.')
    cur.execute("DROP TABLE IF EXISTS mlb_retrosheet_ballparks;")
    
    ## ..and then create the table (see vss_db_tables.py for the code behind the table).
    cur.execute(SQLITE_MLB_RETROSHEET_BALLPARK_TABLE)
    print(f'{datetime.now()}\t[mlb_retrosheet_ballparks] has been created.')


    print(f'{datetime.now()}\tAttempting to download the Retrosheet ballpark data.')
    
    ## This Retrosheet file doesn't have columns, so we have to define them before downloading the text file.
    retrosheet_ballpark_columns=['park_id','park_name','park_alt_name','park_city',
    'park_state','park_start_date','park_end_date','park_leauge','park_notes']
    
    ## TODO: Add a failure condition in the case the internet fails, or something goes horrificly wrong on the user's computer
    retrosheet_ballpark_df = pd.read_csv(vss_urls.RETROSHEET_BALLPARKS,sep=",",header=0,names=retrosheet_ballpark_columns)

    ## Once we have the data, and it's a properly formatted Pandas dataframe, send the data to the SQLite3 instance for Visual Sports Studio.
    print(f'{datetime.now()}\tSuccessfully downloaded the Retrosheet ballpark data. Moving to insert the Retrosheet ballpark data into the SQLite3 database.')
    retrosheet_ballpark_df.to_sql("mlb_retrosheet_ballparks",con,if_exists="append",index=False)
    
    ## This is done to prevent memory leaks. We don't need this data anymore, so we are deleting these variables to free up memory.
    del retrosheet_ballpark_columns
    del retrosheet_ballpark_df
    
    print(f'{datetime.now()}\tSuccessfully inserted the Retrosheet ballpark data into the SQLite3 database.')
    
    con.close()

def sqlite3_retrosheet_ejections(db_dir="temp"):
    """
    Retrives the current Retrosheet ballparks text file,
    converts the file into a Pandas dataframe (read: spreadsheet), 
    and then sends the dataframe to the VSS SQLite3 database.

    Call this fuction only if you want to nuke the existing data. 
    If this function is called, pre-existing data will be deleted!
    
    Args:
        None

    Returns:
        None
    """
    ## Connect to the SQLite instance for Visual Sports Studio (vss_baseball.sqlite).
    con = sqlite3.connect(f"{db_dir}/vss_baseball_retrosheet.sqlite",check_same_thread=True) ## TODO: Make a universal filename for the SQLite instance.
    cur = con.cursor()

    ## Delete the existing table if it exists... 
    print(f'{datetime.now()}\tAttempting to create the [mlb_retrosheet_ejections] table.')
    cur.execute("DROP TABLE IF EXISTS mlb_retrosheet_ejections;")

    ## ..and then create the table (see vss_db_tables.py for the code behind the table).
    cur.execute(SQLITE_MLB_RETROSHEET_EJECTIONS_TABLE)
    print(f'{datetime.now()}\t[mlb_retrosheet_ejections] has been created.')

    print(f'{datetime.now()}\tAttempting to download the Retrosheet ejection data.')
    ## TODO: Add a failure condition in the case the internet fails, or something goes horrificly wrong on the user's computer
    retrosheet_ejection_df = pd.read_csv(vss_urls.RETROSHEET_EJECTIONS,sep=",")

    ## Since this Retrosheet text file has columns, we can re-name the columns here.
    retrosheet_ejection_df.columns = ['game_id','date','dh','ejectee','ejectee_name','team','job','umpire','umpire_name','inning','reason']
    print(f'{datetime.now()}\tSuccessfully downloaded the Retrosheet ejection data. Moving to insert the Retrosheet ejection data into the SQLite3 database.')

    retrosheet_ejection_df.to_sql("mlb_retrosheet_ejections",con,if_exists="append",index=False)

    ## This is done to prevent memory leaks. We don't need this data anymore, so we are deleting these variables to free up memory.
    del retrosheet_ejection_df

    print(f'{datetime.now()}\tSuccessfully inserted the Retrosheet ejection data into the SQLite3 database.')
    
    con.close()

def sqlite3_retrosheet_franchises(db_dir="temp"):
    con = sqlite3.connect(f"{db_dir}/vss_baseball_retrosheet.sqlite",check_same_thread=True)
    cur = con.cursor()

    ## Delete the existing table if it exists...     
    print(f'{datetime.now()}\tAttempting to create the [mlb_retrosheet_franchises] table.')
    cur.execute("DROP TABLE IF EXISTS mlb_retrosheet_franchises;")

    ## ..and then create the table (see vss_db_tables.py for the code behind the table).
    cur.execute(SQLITE_MLB_RETROSHEET_FRANCHISE_TABLE)
    print(f'{datetime.now()}\t[mlb_retrosheet_franchises] has been created.')

    print(f'{datetime.now()}\tAttempting to download the Retrosheet franchise data.')
    ## This Retrosheet file doesn't have columns, so we have to define them before downloading the text file.
    retrosheet_franchise_columns=['fran_id','leauge','city','nickname','first_year','last_year']
    retrosheet_franchise_df = pd.read_csv(vss_urls.RETROSHEET_FRANCHISES,sep=",",header=0,names=retrosheet_franchise_columns)

    ## This is a fix to ensure that [mlb_retrosheet_franchises] can have a primary key column in [mlb_retrosheet_franchises].[fran_id]
    retrosheet_franchise_df = retrosheet_franchise_df[retrosheet_franchise_df['fran_id'] != 'MIL']
    retrosheet_franchise_df = retrosheet_franchise_df[retrosheet_franchise_df['fran_id'] != 'HOU']
    retrosheet_franchise_df.loc[len(retrosheet_franchise_df.index)] = ['HOU','AL','Houston','Astros',1962,datetime.now().year]
    retrosheet_franchise_df.loc[len(retrosheet_franchise_df.index)] = ['MIL','NL','Milwaukee','Brewers',1970,datetime.now().year]
    print(f'{datetime.now()}\tSuccessfully downloaded the Retrosheet franchise data. Moving to insert the Retrosheet franchise data into the SQLite3 database.')
    retrosheet_franchise_df.to_sql("mlb_retrosheet_franchises",con,if_exists="append",index=False)
    
    ## This is done to prevent memory leaks. We don't need this data anymore, so we are deleting these variables to free up memory.
    del retrosheet_franchise_columns
    del retrosheet_franchise_df
    
    ## This is an alternative fix, but due to SQLite3 limitations, this fix isn't an ideal fix.
    # cur.execute("DELETE FROM mlb_retrosheet_franchises WHERE fran_id = \"HOU\" OR fran_id = \"MIL\";")
    # con.commit()

    # cur.execute("INSERT INTO mlb_retrosheet_franchises VALUES ('HOU','AL','Houston','Astros',1962,2022),('MIL','NL','Milwaukee','Brewers',1970,2022)")
    # con.commit()

    print(f'{datetime.now()}\tSuccessfully inserted the Retrosheet franchise data into the SQLite3 database.')

    
    con.close()

def sqlite3_retrosheet_people(db_dir="temp"):
    con = sqlite3.connect(f"{db_dir}/vss_baseball_retrosheet.sqlite",check_same_thread=True)
    cur = con.cursor()

    ## Delete the existing table if it exists...     
    print(f'{datetime.now()}\tAttempting to create the [mlb_retrosheet_people] table.')
    cur.execute("DROP TABLE IF EXISTS mlb_retrosheet_people;")
    
    ## ..and then create the table (see vss_db_tables.py for the code behind the table).
    cur.execute(SQLITE_MLB_RETROSHEET_PEOPLE_TABLE)
    print(f'{datetime.now()}\t[mlb_retrosheet_people] has been created.')

    print(f'{datetime.now()}\tAttempting to download the Retrosheet people data.')
    retrosheet_people_df = pd.read_csv(vss_urls.RETROSHEET_PEOPLE,sep=",",)
    
    ## Since this Retrosheet text file has columns, we can re-name the columns here.
    retrosheet_people_df.columns = ['player_id','last_name','first_name','nickname',
    'birthdate','birth_city','birth_state','birth_country','play_debut',
    'play_last_game','mgr_debut','mgr_last_game','coach_debut',
    'coach_last_game','ump_debut','ump_last_game','death_date',
    'death_city','death_state','death_country','bats','throws',
    'height','weight','cemetery','ceme_city','ceme_state','ceme_country',
    'ceme_note','birth_name','name_chg','bat_chg','hof']
    print(f'{datetime.now()}\tSuccessfully downloaded the Retrosheet people data. Moving to insert the Retrosheet people data into the SQLite3 database.')
    
    retrosheet_people_df.to_sql("mlb_retrosheet_people",con,if_exists="append",index=False)

    ## This is done to prevent memory leaks. We don't need this data anymore, so we are deleting these variables to free up memory.
    del retrosheet_people_df
    print(f'{datetime.now()}\tSuccessfully inserted the Retrosheet people data into the SQLite3 database.')

    
    con.close()

def sqlite3_retrosheet_schedules(db_dir="temp"):
    now = datetime.now()
    current_year = int(now.year)
    retrosheet_schedule_df = pd.DataFrame()
    season_df = pd.DataFrame()
    
    con = sqlite3.connect(f"{db_dir}/vss_baseball_retrosheet.sqlite",check_same_thread=True)
    cur = con.cursor()

    print(f'{datetime.now()}\tAttempting to create the [mlb_retrosheet_schedule] table.')
    cur.execute("DROP TABLE IF EXISTS mlb_retrosheet_schedule;")
    cur.execute(SQLITE_MLB_RETROSHEET_SCHEDULE_TABLE)

    ## This Retrosheet file doesn't have columns, so we have to define them before downloading the text file.
    retrosheet_schedule_columns = ['date_id','game_num','day','away_team_id','away_team_leauge','away_game_num','home_team_id','home_team_leauge','home_game_num','time_of_day','delay_info','makeup_date']

    ## Because Retrosheet divides up their schedule data into 
    ## multiple files, we need to turn those files 
    ## (100+ for schedule data) into one pandas dataframe.
    ## After that's done, we can then insert the downloaded 
    ## data into the SQLite3 database

    ## Effectively, get all schedule data from 1877 to present day.
    for i in range(1877,current_year+1):
        sea = i ## This is done to make it easier to read the function.

        if sea == 2020:
            ######################################################################################
            ## 2020 Weirdness                                                                   ##
            ##----------------------------------------------------------------------------------##
            ## Retrosheet holds two schedule files for 2020:                                    ##
            ##  - 2020REV.TXT = The actual schedule for the 2020 MLB season.                    ##
            ##  - 2020ORG.TXT = The planned schedule for the 2020 MLB season,                   ##
            ##                  prior to that season's delay because of the COVID-19 pandemic.  ##
            ## I may add functionality for the original schedule down the road,                 ##
            ## but that data doesn't any make sense in this table containing historical games.  ##
            ######################################################################################
            url_2020 = "https://raw.githubusercontent.com/chadwickbureau/retrosheet/master/schedule/2020REV.TXT"
            season_df = pd.read_csv(url_2020,header=None,names=retrosheet_schedule_columns)
        else:
            ## If we don't have to worry about 2020 weirdness, we read in every schedule file, one-by-one
            season_df = pd.read_csv(vss_urls.RETROSHEET_SCHEDULES.format(season=sea),header=None,names=retrosheet_schedule_columns)

        ## Deletes rows where [away_team_id] has a null vallue (lack of a value).
        season_df = season_df.dropna(subset=['away_team_id'])
        
        ## If the function is at this point, we have successully downloaded the schedule file.
        ## At this point in the loop, we need to add this data to retrosheet_schedule_df, 
        ## A.K.A the spreadsheet we want to insert into SQLite3.
        retrosheet_schedule_df = pd.concat([retrosheet_schedule_df,season_df])
        
        print(f'{datetime.now()}\t{i} season successfully downloaded.')
    print(f'{datetime.now()}\tSuccessfully downloaded the Retrosheet schedule data. Moving to insert the Retrosheet schedule data into the SQLite3 database.')

    ## Once we have all the schedule data downloaded, insert the data into our SQLite instance.
    retrosheet_schedule_df.to_sql("mlb_retrosheet_schedule",con,if_exists="append",index=False)
    
    ## This is done to prevent memory leaks. We don't need this data anymore, so we are deleting these variables to free up memory.
    del season_df
    del retrosheet_schedule_df
    del now
    del current_year
    del retrosheet_schedule_columns

    print(f'{datetime.now()}\tSuccessfully inserted the Retrosheet schedule data into the SQLite3 database.')
    
    
    con.close()


##############################################################################################################################################
##                                                                                                                                          ##
##  Retrosplits functions                                                                                                                   ##
##------------------------------------------------------------------------------------------------------------------------------------------##
##                                                                                                                                          ##
##      Functions that take data from the retrosplits baseball project,                                                                     ##
##      and puts the resulting data in a SQLite database that a user running                                                                ##
##      Visual Sports Studio can use, and an advanced user can copy/export/use                                                              ##
##      the data with ease.                                                                                                                 ##
##                                                                                                                                          ##
##      The retrosplits project attempts to take the data collected by the Retrosheet baseball project, and put it into CSV files           ##
##       that an advanced user can use for their own personal or business use.                                                              ##
##                                                                                                                                          ##
##############################################################################################################################################

def sqlite3_retrosplits_player_box(db_dir="temp",firstSeason=2020,lastSeason=2022):
    now = datetime.now()
    current_year = int(now.year)
    retrosheet_box_df = pd.DataFrame()
    season_df = pd.DataFrame()
    
    con = sqlite3.connect(f"{db_dir}/vss_baseball_retrosplits.sqlite",check_same_thread=True)
    cur = con.cursor()

    print(f'{datetime.now()}\tsqlite3_retrosplits_player_box\tAttempting to create the [mlb_retrosplits_player_box] table.')
    cur.execute("DROP TABLE IF EXISTS mlb_retrosplits_player_box;")
    cur.execute(SQLITE_MLB_RETROSPLITS_PLAYER_BOX)


    ## Because retrosplits divides up their box stats data into 
    ## multiple files, we need to turn those files 
    ## (100+ for box stats data) into one pandas dataframe.
    ## After that's done, we can then insert the downloaded 
    ## data into the SQLite3 database

    ## Effectively, get all schedule data from 1877 to present day.
    for i in range(firstSeason,lastSeason+1):
        sea = i ## This is done to make it easier to read the function.
        try:
            season_df = pd.read_csv(vss_urls.RETROSPLIT_PLAYER_BOX.format(season=sea))
            print(f'{datetime.now()}\tsqlite3_retrosplits_player_box\t{i} season successfully downloaded. Attempting to insert data into SQLite3 instance.')
            season_df.to_sql("mlb_retrosplits_player_box",con,if_exists="append",index=False)
            print(f'{datetime.now()}\tsqlite3_retrosplits_player_box\tSucessfuly inserted data into SQLite3 instance.')
        except:
            season_df = pd.DataFrame()
            print(f'{datetime.now()}\tsqlite3_retrosplits_player_box\t{i} season was not successfully downloaded.')
        
        
    #print(f'{datetime.now()}\tsqlite3_retrosplits_player_box\tSuccessfully downloaded the Retrosheet player box stats data. Moving to insert the Retrosheet schedule data into the SQLite3 database.')

    ## Once we have all the schedule data downloaded, insert the data into our SQLite instance.
    retrosheet_box_df.to_sql("mlb_retrosplits_player_box",con,if_exists="append",index=False)
    
    ## This is done to prevent memory leaks. We don't need this data anymore, so we are deleting these variables to free up memory.
    del season_df
    del retrosheet_box_df
    del now
    del current_year

    print(f'{datetime.now()}\tsqlite3_retrosplits_player_box\tSuccessfully inserted the Retrosheet player box stats data into the SQLite3 database.')
    
    
    con.close()


def sqlite3_statcast_Pbp(firstSeson:int,lastSeason=int(datetime.now().year),db_dir="temp/"):
    now = datetime.now()
    current_year = int(now.year)
    statcast_df = pd.DataFrame()
    season_df = pd.DataFrame()
    month_df_one = pd.DataFrame()
    month_df_two = pd.DataFrame()


    if firstSeson < 1974:
        firstSeson = 1974
        print('It\'s not possible to get Statcast play-by-play data before 1974 at this time.')
    elif firstSeson > current_year:
        firstSeson = current_year
        print('Please ensure that we are trying to download data that exists, and not data that will exist in the future.')
    con = sqlite3.connect("vss_baseball_pbp.sqlite")
    cur = con.cursor()

    print(f'{datetime.now()}\tAttempting to create the [mlb_statcast_pbp] table.')
    cur.execute("DROP TABLE IF EXISTS mlb_statcast_pbp;")
    cur.execute(SQLITE_MLB_STATCAST_PBP_TABLE)

    ## ~192.34 MB per season
    for i in range(lastSeason,firstSeson-1,-1): # Count down from whatever the current year is, to whatever year the user sets as the oldest season they want.
        season_df = pd.DataFrame()
        sea = i
        print(sea)
        for j in range(3,12): # The latest month MLB games can be played in is November
            
            pbp_month = "0"

            if j < 10:
                pbp_month = f"0{j}"
            else:
                pbp_month = f"{j}"
            
            print(sea,pbp_month)

            #season_df = pd.read_csv(RETROSHEET_SCHEDULES.format(season=sea),header=None,names=retrosheet_schedule_columns)
            try:
                month_df_one = pd.read_csv(vss_urls.STATCAST_PBP_ONE.format(season=sea,month=pbp_month))
            except:
                month_df_one = pd.DataFrame()
                print('Couldn\'t download the PBP file for this month')

            try:
                month_df_two = pd.read_csv(vss_urls.STATCAST_PBP_TWO.format(season=sea,month=pbp_month))
            except:
                month_df_two = pd.DataFrame()
                print('Couldn\'t download the PBP file for this month')
            
            season_df = pd.concat([month_df_one,month_df_two,season_df])
    
            del month_df_one
            del month_df_two
        
        #statcast_df = pd.concat([season_df,statcast_df])

        season_df.to_sql("mlb_statcast_pbp",con,if_exists="append",index=False)
        del season_df
    
    #statcast_df.to_sql("mlb_statcast_pbp",con,if_exists="append",index=False)

def main():
    #sqlite3_retrosplits_player_box(2000)
    #sqlite3_baseball_multithreading()
    sqlite3_baseball_multiprocessing()

if __name__ == "__main__":
    main()