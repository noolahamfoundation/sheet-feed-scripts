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


do_rotate("/home/nat/Documents/Noolaham/Batch9/C99/master")
