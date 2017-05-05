# -*- coding: utf-8 -*-
import os
import sys

noolahamNum = 90
noolahamID = 35090

for batch in ["Batch9"]:
    batchFolder = r"/home/nat/Desktop/NoolahamFinal/" + batch
    batchFolder = r"/home/nat/Documents/Noolaham/" + batch

    for i in range(1,11):
        noolahamNum = noolahamNum + 1
        noolahamID = noolahamID + 1
        pgNoolahamNum = "C" + str(noolahamNum)
        pgNoolahamID = str(noolahamID)

        datadir1 = os.path.join(batchFolder, pgNoolahamNum)
        datadir1ID = os.path.join(batchFolder, pgNoolahamID)
        os.chdir(datadir1)

        os.system("mv " + pgNoolahamNum + ".JPG " + pgNoolahamID + ".JPG")
        os.system("mv " + pgNoolahamNum + "c_.pdf " + pgNoolahamID + ".pdf")

        os.system("mv " + datadir1 + " " + datadir1ID)

        # os.remove(pgNoolahamNum + ".pdf")
        print pgNoolahamID


os.chdir("/home/nat/Desktop/sheet-feed-scripts")