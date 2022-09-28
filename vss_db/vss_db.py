############################################################################################################################################
##
##  vss_db.py
##------------------------------------------------------------------------------------------------------------------------------------------
##
##  TODO: create description of this file.

from .vss_db_baseball import sqlite3_baseball

def sqlite3_startup():
    ## For testing purposes, I am putting the sport tested in here to be able to control wha
    print('This is a test')
    sqlite3_baseball()

## The folllowing code should only run when vss_db.py is run. 
## This needs to be commented out when we are compliling Visual Sports Studio.
def main():
    sqlite3_startup() 

if __name__ == "__main__":
    main()