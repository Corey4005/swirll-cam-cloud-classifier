# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:14:19 2022

@author: cwalker
"""

#imports 
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime



#the filepath to the swirll images:
swirlldata = '../Tensorflow/models/research/object_detection/workspace/swirll_demo/images'

#the filepaths to cloud fraction data
cloud_fraction_swirll_2020 = '../swirll-data/2020_cloud_fraction_swirll.csv'
cloud_fraction_HSV_ASOS_2020 = '../swirll-data/2020_cloud_fraction_HSV_ASOS.csv'

def cloud_fraction_all_imgs():
    '''
    Purpose
    -------
    
    This script reads each image in the 2020 dataset and returns a dataframe 
    with cloud fraction, filepath, and octa score by date. 

    Returns
    -------
    df : Pandas DataFrame
    
        Returns the pandas dataframe for cloud fraction and okta score for each 
        image in the 2020 dataset.
    
    .csv : Excel Workbook
        
        Saves a .csv of the Pandas DataFrame in ../swirll-data/ for easy access
        
    

    '''
    
    dates = []
    file_names = []
    #read all the images and get their name
    for root, directory, file in os.walk(swirlldata):
        for f in file:
            if f.endswith('.jpg'):
        
        #get file name
                filepath = os.path.join(swirlldata, f)
                raw_name = filepath.split('/')[-1]
                date_string = raw_name[-20:]
                img_date = datetime.strptime(date_string, "%Y_%m%d_%H%M%S.jpg")
                dates.append(img_date)
                file_names.append(filepath)
    #make the dataframe
    dic = {'Date' : dates, 'File Names' : file_names}
    df = pd.DataFrame(data=dic)
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    
    #go through the images and read them for cloud fraction
    cloud_fraction = []
    cf_oktas = []
    
    count = 0
    for f in df['File Names']:
        count = count + 1
        
        #read the image
        img_orig = mplim.imread(f)
        
        #limit to sky
        img_orig = img_orig[:,0:1300,:]
        img = np.int16(img_orig)  # Convert image to 16-bit signed int for computation
        cf_img = img[:,:,2] - img[:,:,0]  # Get differece between blue and red
        cf_img = np.where(cf_img < 0, -cf_img, cf_img)  # Absolute value of difference
        cf_img = np.uint8(cf_img)  # Convert back to 8-bit unsigned integer

        #Get number of pixels above threshold percentage
        threshold_percentage = 0.10 # approx 20% experimentally observed
        # threshold_img = (cf_img / 255) > threshold_percentage
        thresh_vals = np.count_nonzero( (cf_img / 255) > threshold_percentage )

        # Calculate cloud fraction in oktas
        cf_okta = 8 - int( ( thresh_vals / cf_img.size ) * 8 )

        # Convert cloud fraction to named cloud cover in oktas
        cf_names = {
                0 : "CLR",
               
                1 : "FEW",
                2 : "FEW",
               
                3 : "SCT",
                4 : "SCT",
               
                5 : "BKN",
                6 : "BKN",
                7 : "BKN",
               
                8 : "OVC"
                }
        
        # get the appropriate octa name 
        cf_name = cf_names[cf_okta]
        
        print('Cloud Cover for image {}:'.format(count), cf_okta, cf_name)
        
        # store data in list
        cloud_fraction.append(cf_name)
        cf_oktas.append(cf_okta)
        
    
    print('All images processed!')
    
    df['Cloud Fraction'] = cloud_fraction
    df['Okta'] = cf_oktas
    
    savepath = '../swirll-data/'
    
    df.to_csv(savepath+'2020_cloud_fraction_swirll.csv')
    
    return df


    
def merge():
    '''

    Returns
    -------
    merged : Pandas DataFrame
        Contains the HSV ASOS Cloud Cover data from the celiometer (weighted 
        average) combined with cloud fraction data from swirll's roundshot.

    '''
    #HSV ASOS 
    df = pd.read_csv(cloud_fraction_HSV_ASOS_2020)
    
    
    #set index to protect format
    df.set_index(df['Date'], inplace=True)
    
    #get datetime
    df.index = pd.to_datetime(df.index)
    
    #format the dates so they merge correctly
    df.index = df.index.strftime('%Y-%m-%d-%H')
    df.index = pd.to_datetime(df.index)
    
    #SWIRLL
    df2 = pd.read_csv(cloud_fraction_swirll_2020)
    
    #set index to protect format
    df2.set_index(df2['Date'], inplace=True)
    
    #get datetime
    df2.index = pd.to_datetime(df2.index)
    
    #format the dates so they merge correctly
    df2.index = df2.index.strftime('%Y-%m-%d-%H')
    df2.index = pd.to_datetime(df2.index)
    
    #class numbers for cloud fractions
    cf_names = {'CLR' : 0, 
                'FEW' : 1, 
                'SCT' : 2, 
                'BKN' : 3, 
                'OVC' : 4, 
                'VV ': np.nan, 
                'M' : np.nan}
    

    
    #lambda function to apply over columns and return number
    get_class = lambda x: cf_names[x]
    
    #get class numbers for swirll dataset
    df2['Swirll Cloud Class'] = df2['Cloud Fraction'].apply(get_class)
    
    
    #get class numbers for HSV dataset
    df['HSV Skyc1 Class'] = df['skyc1'].apply(get_class)
    df['HSV Skyc2 Class'] = df['skyc2'].apply(get_class)
    df['HSV Skyc3 Class'] = df['skyc3'].apply(get_class)
    df['HSV ASOS Cloud Class'] = df[['HSV Skyc1 Class', 'HSV Skyc2 Class', 'HSV Skyc3 Class']].mean(axis=1)
    df = df[['skyc1', 'skyc2', 'skyc3', 'HSV ASOS Cloud Class']]
    
    #drop extra date column
    df2.drop('Date', inplace=True, axis=1)
    
    #get mean data by day if more than one observation per day
    df = df.groupby(df.index).mean()
    df2 = df2.groupby(df2.index).mean()
    
    #reset indexes for merge
    df.reset_index(inplace=True)
    df2.reset_index(inplace=True)
    
    #merge and drop okta
    merged = pd.merge(df2, df, on='Date')
    merged.drop('Okta', axis=1, inplace=True)
    
    #set index
    merged.set_index('Date', inplace=True)
    return merged
    
    
    # return merged