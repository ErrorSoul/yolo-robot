# -*- coding: utf-8 -*-
import os
import sys
import glob


def mover(file, dirs):
    """(str)--->Nonetype
    Find and move files to dir. If not dir, make it.
    
    """
    try:
        if not os.path.isdir(dirs):
            os.mkdir(dirs)
        for file in glob.iglob(file):
            if  os.path.isfile(file):
            
                yield file
                #print dirs, type(dirs)
                #os.system("mv {0} {1}".format(file, dirs))
    finally:
        print "Work complete".center(80, "#")

        

a = mover ('/home/errorsoul/Загрузки/*ython*', "/home/errorsoul/Документы/python")        
