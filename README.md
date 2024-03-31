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

# Clone our version of YOLOv5:
git clone https://github.com/pallavid30/yolov52.git

# Install all needed packages to run yolov5:
cd yolov52/
pip install -r requirements.txt

```
