############################################################################################################################################
##
##  vss_urls.py
##------------------------------------------------------------------------------------------------------------------------------------------
##
##  TODO: create description of this file.

## MLB
RETROSHEET_GITHUB = "https://raw.githubusercontent.com/chadwickbureau/retrosheet/master"
RETROSHEET_SCHEDULES = RETROSHEET_GITHUB+"/schedule/{season}SKED.TXT"
RETROSHEET_BALLPARKS = "https://www.retrosheet.org/parkcode.txt"
RETROSHEET_EJECTIONS = "https://www.retrosheet.org/Ejecdata.txt"
RETROSHEET_PEOPLE = "https://www.retrosheet.org/BIOFILE.TXT"
RETROSHEET_FRANCHISES = "https://www.retrosheet.org/TEAMABR.TXT"
RETROSPLIT_GITHUB = ""

### The files containing pitch-by-pitch statcast data can easily be 60+ MBs, which is above the 50MB file limit that Github wants files to be. 
### As a result, the PBP files are spit in half.
STATCAST_PBP_ONE = "https://raw.githubusercontent.com/sportsdataverse/sportsdataverse-baseball-data/main/gamelogs/{season}_{month}_01_statcast.csv"
STATCAST_PBP_TWO = "https://raw.githubusercontent.com/sportsdataverse/sportsdataverse-baseball-data/main/gamelogs/{season}_{month}_01_statcast.csv"