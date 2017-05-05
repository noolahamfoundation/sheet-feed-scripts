#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import glob
import shutil
from shutil import copyfile

def _getDirs(base):
    return [x for x in glob.iglob(os.path.join( base, '*')) if os.path.isdir(x) ]

def rglob(base, pattern):
    list = []
    list.extend(glob.glob(os.path.join(base,pattern)))
    dirs = _getDirs(base)
    if len(dirs):
        for d in dirs:
            list.extend(rglob(os.path.join(base,d), pattern))
    return list


def runFits(i_folderPath):
    folderPath = i_folderPath
    folderPattern = "*.tiff"

    subFolders = next( os.walk(folderPath) )[1]

    for subFolder in subFolders:
        subFolderPath = folderPath + "/" + subFolder + "/";
        metadataDir = subFolderPath  + "metadata"
        if not os.path.exists(metadataDir):
            os.makedirs(metadataDir)

        print subFolderPath
        tifFiles = rglob(subFolderPath, folderPattern)
        i = 0
        for tifFile in tifFiles:
            print tifFile
            head, tail = os.path.split(tifFile)
            metadataFile = metadataDir + "/" + tail + ".xml"

            i = i + 1
            if i > 5:
                break
            os.chdir("/home/nat/Desktop/fits")
            current = os.getcwd();
            command = "./fits.sh -i " + tifFile + " -o " + metadataFile
            os.system(command)
            os.chdir(current)

        sourceMetadata = folderPath + "/master/metadata"
        targetMetadata = folderPath + "/metadata"
        if os.path.exists(targetMetadata):
            shutil.rmtree(targetMetadata)

        os.system("mv  " + sourceMetadata + " " + folderPath)


noolahamNum = 90
for batch in ["Batch9"]:
    batchFolder = r"/home/nat/Documents/Noolaham/" + batch

    for i in range(1,11):
        noolahamNum = noolahamNum + 1
        pgNoolahamNum = "C" + str(noolahamNum)

        datadir1 = os.path.join(batchFolder, pgNoolahamNum)
        runFits(datadir1)