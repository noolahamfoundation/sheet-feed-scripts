# -*- coding: utf-8 -*-
import ftplib
import os
import csv
import sys
import time

# Uploads the html file to the noolaham server
def uploadToServer(i_session, i_ftppath, i_htmldir, i_noolahamNum, i_file):
    #print "Uploading file: " + i_file

    i_session.cwd("/project/351/")
    if i_noolahamNum in i_session.nlst() : #check if 'foo' exist inside 'www'
        print i_ftppath + " exists"
    else :
        print i_ftppath + " does not exist"
        i_session.mkd(i_noolahamNum)

    i_session.cwd(i_noolahamNum)

    os.chdir(i_htmldir)
    file = open(i_file,'rb')                  		# file to send
    i_session.storbinary('STOR ' + i_file, file)     	# send the file
    file.close()

    return

# Check if directory exists (in current location)
def directory_exists(i_session, dir):
    filelist = []
    i_session.retrlines('LIST',filelist.append)
    for f in filelist:
        if f.split()[-1] == dir and f.upper().startswith('D'):
            return True
    return False

def downloadFile(i_fileURL):
    command = "wget " + i_fileURL + " -P data"
    print "download: " + command
    os.system(command)

def createCoverImage(i_fileName):
    # command = "java -jar LinkTester.jar ccp " + i_fileName
    folderPath, fileName = os.path.split(i_fileName)
    command = "convert -strip " + i_fileName  + "[0] data/" + os.path.splitext(fileName)[0] + ".JPG"
    os.system(command)

session = ftplib.FTP('host','ftpuser','ftppwd')




noolahamNum = 35090
for batch in ["Batch9"]:
    batchFolder = r"/home/nat/Documents/NoolahamFinal/" + batch

    for i in range(1,11):
        noolahamNum = noolahamNum + 1
        pgNoolahamNum = str(noolahamNum)

        datadir = os.path.join(batchFolder, pgNoolahamNum)

        pgFolderPath = "/project/351/" + str(noolahamNum) + "/"
        pgURL = "http://noolaham.net" + pgFolderPath + pgNoolahamNum  + ".pdf"

        print pgURL

        uploadToServer(session, pgFolderPath, datadir, pgNoolahamNum, pgNoolahamNum + ".JPG")
        uploadToServer(session, pgFolderPath, datadir, pgNoolahamNum, pgNoolahamNum + ".pdf")