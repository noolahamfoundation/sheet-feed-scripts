#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import glob

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

def do_rotate(i_folderPath):
    folderPath = i_folderPath
    folderPattern = "*.tiff"

    print "Rotating " + folderPath
    tifFiles = rglob(folderPath, folderPattern)


    for tifFile in tifFiles:
        head, tail = os.path.split(tifFile)
        pageNumber = tail[5:-5]

        os.chdir(folderPath)
        current = os.getcwd();

        command180 = "convert -rotate 180 " +  tifFile + " " + tifFile
        command90 = "convert -rotate 90 " +  tifFile + " " + tifFile
        command90Minus = "convert -rotate -90 " +  tifFile + " " + tifFile

        if (int(pageNumber) % 2 == 0):
            os.system(command90Minus)
        else:
            os.system(command90)
        os.chdir(current)


# Batch Rotate
noolahamNum = 91
for batch in ["Batch9"]:
    batchFolder = r"/home/nat/Documents/Noolaham/" + batch

    for i in range(1,11):
        noolahamNum = noolahamNum + 1
        pgNoolahamNum = "C" + str(noolahamNum)

        datadir1 = os.path.join(batchFolder, pgNoolahamNum)
        datadir1 = datadir1 + "/master"
        do_rotate(datadir1)
        print datadir1
