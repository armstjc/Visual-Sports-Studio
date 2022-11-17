import os
import shutil

try:
    os.mkdir('temp')
except:
    print('Directory already exists.')

shutil.rmtree('temp',ignore_errors=True)
