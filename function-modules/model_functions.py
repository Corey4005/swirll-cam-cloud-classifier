"""
Project Description: 
    
    This module contains functions that can be easily utilized in jupyter notebooks
    for the use of creating object detection models in Tensorflow. 
    
    Note on train_test_split() function:
        
        In order for this funtion to work correctly, images that have been processed
        to .xml files should be saved in a class directiory. Images that correspond
        to the .xml files should be saved in their original .jpg format in the following
        location:
            
            '../Tensorflow/models/research/object_detection/workspace/swirll_demo/images'
            
        
Created on 4/11/23 

@author Corey Walker

contact: 
    
    cdw0063@uah.edu
    
Note: 
    
    Please site the following Github if the functions are used in another analysis and 
    published. 
    
    Github:
        
        https://github.com/Corey4005
    
"""

#imports 
import os
import random
import shutil
import glob
import pandas as pd
import xml.etree.ElementTree as ET



#the filepath to the swirll images:
swirlldata = '../Tensorflow/models/research/object_detection/workspace/swirll_demo/images'

#the filepaths to cloud fraction data
cloud_fraction_swirll_2020 = '../swirll-data/2020_cloud_fraction_swirll.csv'
cloud_fraction_HSV_ASOS_2020 = '../swirll-data/2020_cloud_fraction_HSV_ASOS.csv'

#train and test directories
train_dir = os.path.join(swirlldata, 'train')
test_dir = os.path.join(swirlldata, 'test')

#train and test label data
train_label = os.path.join(train_dir, 'data')
test_label = os.path.join(test_dir, 'data')


###############
## FUNCTIONS ##
###############

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


    