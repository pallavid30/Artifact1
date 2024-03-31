# Supposing you have 1000 data points inside allImages.
# import random
import os
import random
import numpy as np

def listdir_nohidden(path):
        for f in os.listdir(path):
            if not f.startswith('.'):
                yield f

def createBootstrapInstances(index,j,name):
    rootFol = name + "bootstrap2/run" + str(index) +"/"
    selectedSet = set() 

    globalImages = "./AllLabelsFolders/"+str(j)+"/"
    globalLabels = "./AllLabelsFolders/labels/"
    sinkFolImages = rootFol + "set1/images/train/"
    sinkFolLabels = rootFol + "set1/labels/train/"
    # get a list of files inside  allImages/images/, alist,
    a = listdir_nohidden(globalImages)
    alist = []
    for ii in a:
        alist.append(ii)

    name2rval = dict()
    count = len(alist)
    for i in range(count):
        rval = random.randint(0,count-1)
        alist[rval]
        if (rval in selectedSet):
            name2rval[alist[rval]] = name2rval[alist[rval]] + 1
        else:
            name2rval[alist[rval]] = 0
        temp = alist[rval].split(".")
        os.system("cp "+ globalImages + alist[rval] + " " + sinkFolImages + temp[0] + "_" + str(name2rval[alist[rval]]) + ".jpg")
        os.system("cp "+ globalLabels + temp[0] + ".txt" + " " + sinkFolLabels + temp[0] + "_" + str(name2rval[alist[rval]]) + ".txt")
        selectedSet.add(rval)

    # loop through: 
    testvallistindex=[]
    testvallist = []
    for i in range(count):
      if i not in selectedSet:
          testvallist.append(alist[i])
          testvallistindex.append(i)
    tot = len(testvallist)
    partTest = int(np.floor(0.35*tot))
    partVal = tot - partTest

    sinkFolImagesTest = rootFol + "set1/images/test/"
    sinkFolLabelsTest = rootFol + "set1/labels/test/"
    for i in range(partTest):
        temp = testvallist[i].split(".")
        os.system("cp "+ globalImages + testvallist[i] + " " + sinkFolImagesTest)
        os.system("cp "+ globalLabels + temp[0] + ".txt" + " " + sinkFolLabelsTest + temp[0] + ".txt")
    
    sinkFolImagesVal = rootFol + "set1/images/val/"
    sinkFolLabelsVal = rootFol + "set1/labels/val/"
    for i in range(partTest,tot,1):
        temp = testvallist[i].split(".")
        os.system("cp "+ globalImages + testvallist[i] + " " + sinkFolImagesVal)
        os.system("cp "+ globalLabels + temp[0] + ".txt" + " " + sinkFolLabelsVal + temp[0] + ".txt")
    # print("len is: ",len(testvallist))