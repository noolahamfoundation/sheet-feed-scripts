#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import shutil
from shutil import copyfile

noolahamNum = 95
for batch in ["Batch9"]:
    batchFolder = r"/home/nat/Documents/Noolaham/" + batch

    for i in range(1,11):
        noolahamNum = noolahamNum + 1
        pgNoolahamNum = "C" + str(noolahamNum)

        datadir1 = os.path.join(batchFolder, pgNoolahamNum)
        datadir = datadir1 + "/master/"

        if os.path.exists(datadir):
            shutil.rmtree(datadir)
        os.makedirs(datadir)
        sourceTif = datadir1 + "/" + pgNoolahamNum + ".tif"
        targetTif = datadir + pgNoolahamNum + ".tif"
        copyfile(sourceTif, targetTif)

        startPage = 1

        path, dirs, files = os.walk(datadir1).next()
        file_count = len(files)
        if file_count == 3:
            startPage = 2
        elif file_count >= 5:
            startPage = 3

        print "Processing " + datadir

        # Extract the tiff files
        os.chdir(datadir)
        cmdExtractTiff = "convert " + pgNoolahamNum + ".tif -scene " + str(startPage) + " page_%04d.tiff"
        print cmdExtractTiff
        os.system(cmdExtractTiff)

        # Delete the copied tif file
        os.remove(targetTif)

os.chdir("/home/nat/Desktop/sheet-feed-scripts")