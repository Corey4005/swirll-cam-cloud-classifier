# Welcome to swirll-cam-cloud-classifier repo!

The goal of this repository is to provide students at UAH with an opportunity to collaborate on a github project developing a cloud classifier for the SWIRLL roundshot camera. 

# Task List
- [x] Download raw cloud image dataset and share to this repo.
- [ ] Create labeled cloud database for other end-users in SWIRLL.
- [ ] Develop science questions for object detection of clouds.  
- [ ] Engineer some object detection models for cloud detection and provide documentation.
- [ ] Deploy models to application and demonstrate cloud detection use-cases using computer vision. 

# Credits for Image Labeler Used in This Project 
- We use the image labeler found in [this](https://github.com/tzutalin/labelImg) repo, which was built by [*Tzuta Lin*](https://tzutalin.github.io/). 

### Pull Image labeler to local directory
```
mkdir imglabeler
git clone https://github.com/tzutalin/labelImg.git
```
### How to start the image labeler Anaconda + Windows
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
