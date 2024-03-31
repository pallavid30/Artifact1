import os
import sys
# creation2.py
def creation2(name):
    print("I am here!")
    currDir = os.getcwd()
    os.chdir(name)
    os.system("rm -rf jobs/")
    os.mkdir("jobs")
    os.chdir("jobs")
    homeDir = os.path.expanduser('~')
    

    for i in range(525):
        file = open("run"+str(i)+".sh","w")
        bigString='''#!/bin/bash

# Copy/paste this job script into a text file and submit with the command:
#    sbatch thefilename

#SBATCH --time=00:59:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=9   # 9 processor core(s) per node 
#SBATCH --mem=16G   # maximum memory per node
#SBATCH cp -r /path/to/images .
--gres=gpu:v100:1
#SBATCH --partition=gpu    # gpu node(s)
#SBATCH --job-name="run''' + str(i) + '''"
#SBATCH --mail-user=pallavid@iastate.edu   # email address
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --output="out%j.txt" # job standard output file (%j replaced by job id)
#SBATCH --error="err%j.txt" # job standard error file (%j replaced by job id)

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE
mkdir ''' + name + '''bootstrap2/
cd ''' + name + '''bootstrap2/
rm -rf run''' + str(i) +'''
mkdir run''' + str(i) + '''

mamba init bash
source '''+ homeDir +'''.bashrc
mamba activate yolo

cd ..
python3 allImages2set.py '''+ str(i) + ''' ''' + name + '''  

cd ''' + name + '''bootstrap2/
cd run''' + str(i) +'''/
git clone git@github.com:pallavid30/yolov52.git
cp '''+ currDir + '''data.yaml yolov5/data/
cp '''+ currDir + '''dataloaders.py yolov5/utils/


cd ''' + name + '''bootstrap2/run'''+ str(i) + '''/yolov5/
cp /source/path/to/best.pt .
python3 train.py --hyp 'hyp.VOC.yaml' --img 640 --batch 16 --epochs 2500 --data data.yaml --weights  /work/smryan-scratch/fine_tuning_backbone_10_layers/best.pt --cache --freeze 10
python3 val.py --data data.yaml --weights runs/train/exp/weights/best.pt --img 640 --task test
'''
        file.write(bigString)
        file.close()

if __name__ == "__main__":
    pathName = int(sys.argv[1])
    print("I am the great hero of all time and space!!!")
    creation2(pathName)