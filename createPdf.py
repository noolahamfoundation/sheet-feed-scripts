#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

noolahamNum = 98

for batch in ["Batch9"]:
    batchFolder = r"/home/nat/Documents/Noolaham/" + batch

    for i in range(1,11):
        noolahamNum = noolahamNum + 1
        pgNoolahamNum = "C" + str(noolahamNum)


        datadir1 = os.path.join(batchFolder, pgNoolahamNum)
        os.chdir(datadir1)

        tifFile = datadir1 + "/" + pgNoolahamNum + ".tif";

        cmdCreatePdf = 'tiff2pdf -o ' + pgNoolahamNum + '.pdf ' + tifFile
        # os.system(cmdCreatePdf)

        print pgNoolahamNum

        # cmdCompress = 'convert -density 250x250 -quality 90 -compress JPEG ' + str(noolahamID) + '.pdf' + ' ' + str(noolahamID) + 'c.pdf'

        cmdCompress = 'gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dColorImageResolution=170 -sOutputFile=' + pgNoolahamNum + 'c_.pdf' + ' ' + pgNoolahamNum + '.pdf'
        os.system(cmdCompress)
        break



os.chdir("/home/nat/Desktop/sheet-feed-scripts")