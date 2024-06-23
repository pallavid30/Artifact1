# Deep Learning-Powered Visual Inspection for Metal Surfaces – Impact of Annotations on Algorithms based on Defect Characteristics

# Abstract

In general, the labeling process provides a set of annotations that are used for supervised learning. A major assumption of this process is that each annotation represents the ground truth about an observed phenomenon, which is defined by manually labeling it. While most extant Deep Learning (DL) research is focused on improving the accuracy and efficiency of training and inferencing algorithms, only limited attention has been paid to data validation. Potential inconsistencies in the labeling process for DL are in this less investigated category. This study assessed the performance of You Only Look Once version 5 small (YOLOv5s) using confidence intervals (CIs) for each defect type in a metal defect benchmark dataset, GC10 DET. The impacts of standardizing the labeling process and the role of consistency in labeling were evaluated through an experimental study. The results showed that individually labeled small-size defects with precise bounding boxes perform better than defects labeled inconsistently in a group. Improved data validation through precise labeling increased average precision (AP) by 12–26% across defect categories. This overall result points to the need for further evaluation of an image dataset through data validation before comparing algorithms on a benchmark dataset and using bootstrap CIs when categories have limited data. 

# Getting started

```bash
# Assuming a bash shell 
git clone https://github.com/pallavid30/Artifact1.git
cd Artifact1



# Install Mamba if you haven't already
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh

# Create a new mamba envrironment, and clone a version of yolov5 that we use throughout:
mamba create -n yolo python=3.9.16
mamba activate yolo
# Clone our version of YOLOv5:
git clone https://github.com/pallavid30/yolov52.git

# Install all needed packages to run yolov5:
cd yolov52/
pip install -r requirements.txt
cd ..

# Next to create a bootstrap instance:
python3 creation2.py "/path/to/where/you/want/the/jobs/" numberOfBootstrapInstances

# For example, I use:
# python3 creation2.py "/work/smryan-scratch/fine_tuning_backbone_10_layers/" 500

# Copy the global set of images to this path to a folder named AllLabelsFolder.
# The folder structure should be as follows:
#--- AllLabelsFolder
#    |
#    |
#    ----- 1
#    |
#    |
#    ----- labels
# where AllLabelsFolder/1/ contains all the images, and AllLabelsFolder/labels/ contains the labels
# Find the example in our repo.

```

# Notes
1. This work uses [Yolov5](https://github.com/ultralytics/yolov5) at a particular commit, which we pull from a separate repository, as [yolov52](https://github.com/pallavid30/yolov52).
2. This work uses the [GC10DET data set](https://www.kaggle.com/datasets/alex000kim/gc10det)
