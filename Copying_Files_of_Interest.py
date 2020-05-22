# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 11:35:23 2020
Moving files of interest
@author: aaron.meneghini
"""

import os, sys, string
from shutil import copyfile


filetype = "tif"
ending = -3
string_Criteria2 = 25

#folder containing thousands of files to be searched
path = "F:\\me_60cm_tif_2018\\"

#destination of selected files
destination = "F:\\NAIP\\"

#make list of files
files = os.listdir(path)

#iterate over list
for f in files:

    if f[ending:] == "tif":

        if f[string_Criteria2] == "6" or f[string_Criteria2]=="7":
            print (f)
            copyfile(path+f, destination+f)
        else:
            next
    else:
        next