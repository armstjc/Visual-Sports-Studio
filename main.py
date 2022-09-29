############################################################################################################################################
##
##  main.py
##------------------------------------------------------------------------------------------------------------------------------------------
##
##  TODO: create description of this file.

import wx
from vss_db.vss_db_baseball import main as a

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(1280, 720))


def main():

    app = wx.App()
    
    ex = Example(None, title='Sizing')
    ex.Show()
    a()
    app.MainLoop()
    

if __name__ == '__main__':
    main()