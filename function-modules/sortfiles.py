'''
@author Corey Walker

contact: cdw0063@uah.edu

Purpose: 
    sortfiles.py takes in a directory tree of images sorted by month and returns
    a flattened directory relative to the module called 
    ..Tensorflow/workspace/swirll_demo/images
    
Parameters: 
    DATAPATH:
        Input the local path to the roundshot images you want to flatten. 

Note: 
    Please site this module if used in another analysis and 
    published. 
    
'''

import os

DATAPATH = ' ### ENTER DATAPATH HERE ### ' 

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
MOVEDIR = '../Tensorflow/workspace/swirll_demo/images/'

#join movedir with the cwd
MOVEDIRBASEJOIN = os.path.join(os.getcwd(), MOVEDIR)

#loop to move files from filelist to MOVEDIRBASEJOIN
for f in FILELIST:
    jpg = f[-20:]
    os.rename(f, MOVEDIRBASEJOIN + jpg)