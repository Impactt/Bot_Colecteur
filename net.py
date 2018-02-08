# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:58:45 2018

@author: fmuret
"""

# =============================================================================
# import urllib.request
# from html.parser import HTMLParser
# 
# with urllib.request.urlopen("http://sebastienguillon.com/test/javascript/convertisseur.html") as url:
#     s = url.read()
# #I'm guessing this would output the html source code?
# print(s)
# =============================================================================
import win32api, win32con, time, random, numpy
from PIL.Image import Image
import PIL.Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.ndimage
import scipy
import numpy as np
from resizeimage import resizeimage
import random
from time import sleep
import threading
from pynput import keyboard
import threading, msvcrt
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageGrab
import os

sys.path.append(os.path.abspath("C:/Users/fmuret/Documents/Florent/python/click_project"))  #path to the fonction file
from fonctions import *



img = cv2.imread('map5.jpg',0)
first=treatment_nvgris(95,img)

thresdown=1050000
threshold=1225000

value=treatment_localisation(first,thresdown,threshold)

second = cv2.imread('map5.jpg')
display_Found(second,value)



    
    
    
    
    
    
    
    
    








