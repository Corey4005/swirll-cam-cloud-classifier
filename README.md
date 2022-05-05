# Welcome to swirll-cam-cloud-classifier repo!

The goal of this repository is to provide students at UAH with an opportunity to collaborate on a github project developing a cloud classifier for the SWIRLL roundshot camera, as well as provide a sample methodology. 

# Download repo to your local machine:
```
git pull https://github.com/Corey4005/swirll-cam-cloud-classifier.git
```

# Credits for Image Labeler Used in This Project 
- We use the image labeler found in [this](https://github.com/tzutalin/labelImg) repo, which was built by [*Tzuta Lin*](https://tzutalin.github.io/) to label cloud classes in SWIRLL images. We have simply copied the code from their repo into this one so all important codes can be pulled together. 
- There is documentation on the how to use the image labeler in the [imglabeler](https://github.com/Corey4005/swirll-cam-cloud-classifier/tree/main/Tensorflow/addons/imglabeler) directory of this repo. 

# Credits for Compute Resources 
This work was made possible in part by a grant of high performance computing resources and technical support from the [Alabama Supercomputer Authority](https://hpcdocs.asc.edu/).

# Cloud Mask Tool 
Individual images from the SWIRLL roundshot camera can be masked, returning the cloud fraction in Oktas using the [plot_cloudfraction.py](https://github.com/Corey4005/swirll-cam-cloud-classifier/blob/main/function-modules/plot_cloudfraction.py) script. A demonstration of this can be found on [line 14](https://github.com/Corey4005/swirll-cam-cloud-classifier/blob/main/demo-notebooks/SWIRLLCAM-Demo.ipynb) of the SWIRLLCAM-Demo Jupyter Notebook. Providing a simple filepath to the image of interest, a two-line command can be passed to a Jupyter Notebook cell which generates the raw and "blue sky characterization" (a measure of how much of the image is sky and how much is cloud). 

# Object Detection Model 
The fair-weather-cumulus object detector was trained on Tensorflow 1.14.0 using the [ssd_mobilenet_v1_coco model](https://github.com/tensorflow/models/blob/master/research/object_detection/samples/configs/ssd_mobilenet_v1_coco.config). This is a convolutional neural network which seperates standard convolution into two steps described in the figure 2 below: 

<p align="center">
  <img 
    width="450"
    height="600"
    src="https://github.com/Corey4005/swirll-cam-cloud-classifier/blob/main/demo-notebooks/images/depth-wise-vs-point.PNG"
  >
</p>

Standard convolution kernals contain a width *D<sub>k</sub>*, a height *D<sub>k</sub>* and a depth *M*. These kernals are applied to an image with horizontal width *D<sub>f</sub>* and vertical height *D<sub>f</sub>*, *N<sup>2</sup>* times producting a feature map *G* with computational cost of *D<sub>k</sub> x D<sub>k</sub> x M x N x D<sub>f</sub> x D<sub>f</sub>.* The ssd_mobilenet_v1_coco model breaks this standard method into two steps: pairwise and depthwise convolutions. This resuls in a computational cost of *D<sub>k</sub>* x *D<sub>k</sub>* x *M* x *D<sub>f</sub>* x *D<sub>f</sub>* + *M* x *N* x *D<sub>f</sub>* x *D<sub>f</sub>*. Ratioing the two-step cost by the standard and canceling like-terms results in a 9-time, less-computationally expensive training algorithm. The linear algebra deriving this intuition is explained in greater detail by *Howard et. al's team* at Google in section 3.1 of their paper titled [*MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*](https://arxiv.org/pdf/1704.04861.pdf).



