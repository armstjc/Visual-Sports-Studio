##############################################################################################################################################
##                                                                                                                                          ##
##  vss_db.py                                                                                                                               ##
##------------------------------------------------------------------------------------------------------------------------------------------##
##                                                                                                                                          ##
##  Author:         Joseph Armstrong (armstjc@mail.uc.edu)                                                                                  ##
##  Description:    This is a placeholder file for testing databases, and functions related to databases.                                   ##
##                                                                                                                                          ##
##############################################################################################################################################

from .vss_db_baseball import sqlite3_baseball_multithreading as a

def sqlite3_startup():
    ## For testing purposes, I am putting the sport tested in here to be able to control wha
    print('This is a test')
    a()

# # The folllowing code should only run when vss_db.py is run. 
# # This needs to be commented out when we are compliling Visual Sports Studio.
# def main():
#     sqlite3_startup() 

# if __name__ == "__main__":
#     main()