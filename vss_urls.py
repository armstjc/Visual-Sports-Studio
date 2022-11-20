##############################################################################################################################################
##                                                                                                                                          ##
##  vss_urls.py                                                                                                                             ##
##------------------------------------------------------------------------------------------------------------------------------------------##
##                                                                                                                                          ##
##  Author:         Joseph Armstrong (armstjc@mail.uc.edu)                                                                                  ##
##  Description:    Houses stock URLs that can be used by other parts of the app.                                                           ##
##                                                                                                                                          ##
##############################################################################################################################################


##############################################################################################################################################
## MLB
##############################################################################################################################################

##############################################################################################################################################
## Retrosheet

RETROSHEET_GITHUB = "https://raw.githubusercontent.com/chadwickbureau/retrosheet/master"

RETROSHEET_SCHEDULES = RETROSHEET_GITHUB + "/schedule/{season}SKED.TXT"
RETROSHEET_BALLPARKS = "https://www.retrosheet.org/parkcode.txt"
RETROSHEET_EJECTIONS = "https://www.retrosheet.org/Ejecdata.txt"
RETROSHEET_PEOPLE = "https://www.retrosheet.org/BIOFILE.TXT"
RETROSHEET_FRANCHISES = "https://www.retrosheet.org/TEAMABR.TXT"

##############################################################################################################################################
## Retrosplits


RETROSPLIT_GITHUB = "https://raw.githubusercontent.com/chadwickbureau/retrosplits/master"
RETROSPLIT_PLAYER_BOX = RETROSPLIT_GITHUB + "/daybyday/playing-{season}.csv"
RETROSPLIT_TEAM_BOX = RETROSPLIT_GITHUB + "/daybyday/teams-{season}.csv"
RETROSPLIT_HEAD_TO_HEAD = RETROSPLIT_GITHUB + "/splits/headtohead-{season}.csv"
RETROSPLIT_BATTIN_BY_POSITION = "https://raw.githubusercontent.com/chadwickbureau/retrosplits/master/splits/batting-byposition-1974.csv"
RETROSPLIT_BATTING_BY_RUNNERS = RETROSPLIT_GITHUB + "/splits/batting-byrunners-{season}.csv"
RETROSPLIT_BATTING_BY_PLATOON = RETROSPLIT_GITHUB + "/splits/batting-platoon-{season}.csv"

RETROSPLIT_PITCHING_BY_RUNNERS = RETROSPLIT_GITHUB + "/splits/pitching-byrunners-{season}.csv"
RETROSPLIT_PITCHING_BY_PLATOON = RETROSPLIT_GITHUB + "/splits/pitching-platoon-{season}.csv"

### The files containing pitch-by-pitch statcast data can easily be 60+ MBs, which is above the 50MB file limit that Github wants files to be. 
### As a result, the PBP files are spit in half.
STATCAST_PBP_ONE = "https://raw.githubusercontent.com/sportsdataverse/sportsdataverse-baseball-data/main/gamelogs/{season}_{month}_01_statcast.csv"
STATCAST_PBP_TWO = "https://raw.githubusercontent.com/sportsdataverse/sportsdataverse-baseball-data/main/gamelogs/{season}_{month}_01_statcast.csv"