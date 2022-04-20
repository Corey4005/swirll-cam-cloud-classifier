"""
Project Description: 
    
    This module contains functions that can be easily utilized in jupyter notebooks
    for the use of creating object detection models in Tensorflow. 
    
Created on 4/11/23 

@author Corey Walker

contact: 
    
    cdw0063@uah.edu
    
Note: 
    
    Please site this module if the functions are used in another analysis and 
    published. 
    
"""

#imports 
import os
import random
import shutil
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.image as mplim
import numpy as np
from datetime import datetime

#the filepath to the swirll images:
swirlldata = '../Tensorflow/workspace/swirll_demo/images'

#train and test directories
train_dir = os.path.join(swirlldata, 'train')
test_dir = os.path.join(swirlldata, 'test')

#train and test label data
train_label = os.path.join(train_dir, 'data')
test_label = os.path.join(test_dir, 'data')


def train_test_split(class_dir, split=None):
    '''
    

    Parameters
    ----------
    class_dir : str
        
        Input the name of the class directory containing the .xml files you wish 
        to split into training and testing partions. 
        
        example directory: 
            class_dir = '../Tensorflow/workspace/swirll_demo/images/fair-weather-cumulus/'
            #Pass the class_dir object to the argument in the function. 
            
    split : float
    
        Input the split percentage. The default is None, but will not work 
        unless an argument is passed.
        
        example split:
            
            0.7 #for a split of 70% training and 30% testing. 

    Returns
    -------
    test : Directory containing model test images
    
        '../Tensorflow/workspace/swirll_demo/images/test'
    
    train : Directory containing model training images
        
        '../Tensorflow/workspace/swirll_demo/images/train'
    

    '''
    #make train and test directories if they do not exist to split into. 
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    
    #create some lists to store info in
    xmls = []
    jpg_xml_paths = []
    
    #get the classes that were developed for splitting in their own list and
    #avoid the test and train directories. 
    for root, directory, files in os.walk(class_dir):
    #get all the .xml files. 
        for f in files:
            if f.endswith('.xml'):
                abpath = os.path.join(root, f)
                xmls.append(abpath)
    
    #create a list of jpgs in images directory that correspond to .xmls and 
    #append to images
    for xml in xmls: 
        jpg = xml[-30:-4]+'.jpg'
        jpg_path = os.path.join(swirlldata, jpg)
        jpg_xml_paths.append((jpg_path, xml))
       
    #shuffle the images
    random.shuffle(jpg_xml_paths)
    
    #create the length of the class_dir 
    class_len = len(jpg_xml_paths)
    
    #training length
    train_len = round(class_len*split)
    print('the length pf your training is :', train_len)
    
    #testing length
    test_len = class_len - train_len
    print('the length of your testing is :', test_len)
    
    #get the individual filepaths that are now in correct order for spliting
    all_jpgs = [f[0] for f in jpg_xml_paths]
    all_xmls = [f[1] for f in jpg_xml_paths]
    
    #partition by split ratio to 
    training_jpgs = all_jpgs[0:train_len]
    testing_jpgs = all_jpgs[-test_len:]
    training_xmls = all_xmls[0:train_len]
    testing_xmls = all_xmls[-test_len:]
    
    #send to appropriate directory
    for f in training_jpgs:
        shutil.copy(f, train_dir)
    
    for f in testing_jpgs:
        shutil.copy(f, test_dir)
    
    for f in training_xmls:
        shutil.copy(f, train_dir)
    
    for f in testing_xmls:
        shutil.copy(f, test_dir)


def xml_to_csv(path):
    '''
    
    Purpose
    -------
    Converts xml files in a directory to .csv label files to be used in 
    tensorflow models. 
    
    Parameters
    ----------
    path : Str 
        Input the path object to the .xml files 

    Returns
    -------
    xml_df : .csv file containing labels with relevant file information for 
    model training. 
    

    '''
    #create data directories if they do not not exist
    if not os.path.exists(train_label):
        os.makedirs(train_label)
    
    if not os.path.exists(test_label):
        os.makedirs(test_label)
    
    #create a list to store .xml values
    xml_list = []
    
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            
            xml_list.append(value)
    
    #create the pandas dataframe and make a file containing the labels
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df
    
def run_xml_to_csv():
    '''
    Purpose
    -------
    Runs the xml_to_csv() function in functions.py for train and test directories
    located in the images directory of swirldemo.
    

    Returns
    -------
    One .csv file for both train and test directories containing the labels for 
    independent .xml files. 

    '''
    
    for directory in ['train','test']:
        image_path = os.path.join(swirlldata, '{}/'.format(directory))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(image_path + 'data/{}_labels.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')
    

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
        threshold_percentage = 0.10  # approx 20% experimentally observed
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
    
    
    
    
