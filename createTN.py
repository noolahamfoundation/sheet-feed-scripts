#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys


noolahamNum = 90

for batch in ["Batch9"]:
    batchFolder = r"/home/nat/Documents/Noolaham/" + batch

    for i in range(1,11):
        noolahamNum = noolahamNum + 1
        pgNoolahamNum = "C" + str(noolahamNum)

        print "Creating TN for " + pgNoolahamNum

        datadir1 = os.path.join(batchFolder, pgNoolahamNum)
        os.chdir(datadir1 + "/master")

        copyfile("page_0001.tiff", "1_page_0001.tiff")
        cmd_clean_TN_Src = 'mogrify -trim 1_page_0001.tiff'
        os.system(cmd_clean_TN_Src)
        cmd_create_TN = ' convert 1_page_0001.tiff -compress JPEG -quality 80 page_0001.JPG'
        os.system(cmd_create_TN )
        os.system("mv page_0001.JPG " + datadir1)
        os.remove("1_page_0001.tiff")
        os.chdir(datadir1)
        os.system("mv page_0001.JPG " + pgNoolahamNum + ".JPG")


os.chdir("/home/nat/Desktop/sheet-feed-scripts")