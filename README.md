# Welcome to swirll-cam-cloud-classifier repo!

The goal of this repository is to provide students at UAH with an opportunity to collaborate on a github project developing a cloud classifier for the SWIRLL roundshot camera, as well as provide a sample methodology. 

# Task List and Progress
- [x] Download raw cloud image dataset and share to this repo.
- [ ] Create labeled cloud database for other end-users in SWIRLL.
- [ ] Develop a module of functions that are useful for object detection of clouds and share to this repo.  
- [ ] Analyze multiple [object detection models](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) for cloud detection and provide Jupyter notebook documentation.
- [ ] Deploy models to application and demonstrate cloud detection use-cases using computer vision. 

# Credits for Image Labeler Used in This Project 
- We use the image labeler found in [this](https://github.com/tzutalin/labelImg) repo, which was built by [*Tzuta Lin*](https://tzutalin.github.io/) to label cloud classes in SWIRLL images. 

### How to pull image labeler to your local directory
```
mkdir imglabeler
git clone https://github.com/tzutalin/labelImg.git
```
### How to start the image labeler with Anaconda + Windows
```
conda install pyqt=5
conda install -c anaconda lxml
pyrcc5 -o libs/resources.py resources.qrc
python labelImg.py
python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```
# Updates 
Date | Update 
|---|---| 
| 3/21/2022 | Cloud data has been selected for labeling from the SWIRRL roundshot camera from the archive. Files were renamed in the download tree and moved to a single directory location using [this](./data/sortfiles.py) script. |
| 3/23/2022 | Directions and location of raw image data for downloading to your local machine can be found [here](./data/README.md). |
| 4/4/2022 | A train-test-split function developed for labeled cumulus versus non-cumulus classes is demonstrated in a Jupyter notebook found [here](https://github.com/Corey4005/swirll-cam-cloud-classifier/blob/main/notebooks/label_and_split_images.ipynb) |
