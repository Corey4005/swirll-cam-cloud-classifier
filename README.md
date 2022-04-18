# Welcome to swirll-cam-cloud-classifier repo!

The goal of this repository is to provide students at UAH with an opportunity to collaborate on a github project developing a cloud classifier for the SWIRLL roundshot camera, as well as provide a sample methodology. 

# Download repo to your local machine:
```
git pull https://github.com/Corey4005/swirll-cam-cloud-classifier.git
```

# Credits for Image Labeler Used in This Project 
- We use the image labeler found in [this](https://github.com/tzutalin/labelImg) repo, which was built by [*Tzuta Lin*](https://tzutalin.github.io/) to label cloud classes in SWIRLL images. We have simply copied the code from their repo into this one so all important codes can be pulled together. 
- There is documentation on the how to use the image labeler in the [imglabeler](https://github.com/Corey4005/swirll-cam-cloud-classifier/tree/main/imglabeler) directory of this repo. 

# Task List and Progress
- [x] Download raw cloud image dataset and share to this repo.
- [ ] Create labeled cloud database for other end-users in SWIRLL.
- [ ] Develop a module of functions that are useful for object detection of clouds and share to this repo.  
- [ ] Analyze multiple [object detection models](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) for cloud detection and provide Jupyter notebook documentation.
- [ ] Deploy models to application and demonstrate cloud detection use-cases using computer vision. 

# Updates 
Date | Update 
|---|---| 
| 3/21/2022 | Cloud data has been selected for labeling from the SWIRRL roundshot camera from the archive. Files were renamed in the download tree and moved to a single directory location using [this](./function-modules/sortfiles.py) script. |
| 3/23/2022 | Directions and location of raw image data for downloading to your local machine can be found [here](./swirll-data/README.md). |
| 4/13/2022 | [Tensorflow models](https://github.com/Corey4005/swirll-cam-cloud-classifier/tree/main/Tensorflow/models) were downloaded and added to this repository for ease of access. |
| 4/18/2022 | A custom .xml to .csv function for the labeled image data has been added to [functions.py](https://github.com/Corey4005/swirll-cam-cloud-classifier/blob/main/function-modules/functions.py) to make labels for Tensorflow models. A custom train-test-split function also has been successfully developed that works with the file structure in this repository |

