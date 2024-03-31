# 5 runs
from createBootstrapInstances import createBootstrapInstances 
import os
import sys
# img_07_425503000_00061.txt
def runner(i,name):
    rootFol = name + "bootstrap2/run" + str(i) +"/"
    os.system("rm -rf " + rootFol + "set1/")
    os.mkdir(rootFol +"set1/")
    os.mkdir(rootFol +"set1/images")
    os.mkdir(rootFol +"set1/images/test")
    os.mkdir(rootFol +"set1/images/train")
    os.mkdir(rootFol +"set1/images/val")
    os.mkdir(rootFol +"set1/labels")
    os.mkdir(rootFol +"set1/labels/test")
    os.mkdir(rootFol +"set1/labels/train")
    os.mkdir(rootFol +"set1/labels/val")
    for j in range(1,11,1):
        createBootstrapInstances(i,j,name)
    filesInTrain = os.listdir(rootFol +"/set1/images/train/")
    filesInTest = os.listdir(rootFol + "/set1/images/test/")
    filesInVal = os.listdir(rootFol +"/set1/images/val/")
    print("Run" + str(i) +": \n", "train:" + str(len(filesInTrain)))
    print("Run" + str(i) +": \n", "test:" + str(len(filesInTest)))
    print("Run" + str(i) +": \n", "val:" + str(len(filesInVal)))

if __name__ == "__main__":
    i = int(sys.argv[1])
    name = sys.argv[2]
    print("I am the great hero of all time and space!!!")
    runner(i,name)
