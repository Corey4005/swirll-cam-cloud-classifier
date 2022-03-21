import os

#local path to the roundshot images Nate sent me from SWIRLL
DATAPATH = 'C:/Users/cwalker/Downloads/Unconfirmed 685955/tor2/Roundshot/2020'

#join datapath with cwd
DATAPATHBASEJOIN = os.path.join(os.getcwd(), DATAPATH)

#creating a storage location for the files
FILELIST = []

#loop through the files in the join path, get all .jpg and store in filepath
for root, dirs, files in os.walk(DATAPATHBASEJOIN):
    for file in files:
        if(file.endswith('.jpg')):
            FILENAME = os.path.join(root, file)
            FILELIST.append(FILENAME)

#the local directory I want to move all the .jpgs to
MOVEDIR = 'C:/Users/cwalker/Desktop/swirlldata/'

#join movedir with the cwd
MOVEDIRBASEJOIN = os.path.join(os.getcwd(), MOVEDIR)

#loop to move files from filelist to MOVEDIRBASEJOIN
for f in FILELIST:
    jpg = f[-20:]
    os.rename(f, MOVEDIRBASEJOIN + jpg)