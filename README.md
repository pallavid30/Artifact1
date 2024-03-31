# Paper title

# Abstract

- Must contain the link to the paper and other things.

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
