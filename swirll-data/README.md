# How to Download Raw Image Database:
- Raw images used in the models developed in this repository can be downloaded from the zip folder [here](https://drive.google.com/drive/folders/1ZVUGHQ_WykSVkGDCM_sx8CVocxoN4CeF?usp=sharing). 
- Directions for downloading images from the UAH SWIRLLCam image archive can be accessed at [this](https://www.nsstc.uah.edu/swirll/cams/swirll/loopgen/) website.

# Metadata
- Number of images: 1503
- Date of images: 01-01-2020 / 12-30-2020
- Latitude: 34.723° N
- Longitude: 86.642° W
- Elevation: 696ft
- File Naming Convention: 'Swirlldata' + YY-MM-dd + Zulu Time + '.jpg'
- Image Dimensions: 10771 x 2048
- Horizontal Resolution: 72 dpi
- Vertical Resolution: 72 dpi
- Color Representation: sRGB

# Cloud Fraction Data
- [2020_cloud_fraction_swirll.csv](https://github.com/Corey4005/swirll-cam-cloud-classifier/blob/main/swirll-data/2020_cloud_fraction_swirll.csv) contains the okta measurements and cloud fraction for each image in the Raw Image database above. The function used to calculate this data is called `cloud_fraction_all_imgs()` in the [functions.py](https://github.com/Corey4005/swirll-cam-cloud-classifier/blob/main/function-modules/functions.py) module. 
