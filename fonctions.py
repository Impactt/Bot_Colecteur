# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:49:19 2018

@author: fmuret
"""

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
import os.path


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    




def securite(porte,max,min):
    while porte < min or porte > max:    
        porte=int(input("valeur de range entre 1 et 4 ?   "))
        print( porte ) 
    return porte



# #---------------- filtre ----------------------    
def filtrer():
    lena = PIL.Image.open("map.jpg")    #image
    img = np.asarray(lena)  
    img_modified = scipy.ndimage.filters.gaussian_filter(img, sigma=0.7)    #filtre
    reverse=PIL.Image.fromarray(img_modified,'RGB')
    im=reverse
    Image.show(im)
 
    
    
def decision(pos_x,pos_y):
    actualx=pos_x
    actualy=pos_y
        
    direction = random.randint(1,4)
        
    if direction == 1:                          # ==>
        actualx=pos_x+1
    elif direction==2:                          # <==
        actualx=pos_x-1
    elif direction==3:                          #  ^
        actualy=pos_y+1
    elif direction==4:                          #  v
        actualy=pos_y-1
    return (actualy, actualx,direction)
    


def directions(direction):
    if direction==1:                            # ==>
        click(2309, 33)
    elif direction==2:                          # <==
        click(2959, 509)
    elif direction==3:                          #  ^
        click(2299 ,1021)
    else :                                      #  v
        click(1701, 446)
    print(pos_x,pos_y)



def interupt(timer):
    s=timer
    for k in range(0,s):
        n = win32api.GetAsyncKeyState(win32con.VK_F2 )
        if n==-32767:
            return False
            break
        time.sleep(0.1)
    return True




def capture_frame():
    img = ImageGrab.grab(bbox=(0, 0, 1678, 1043)) #x, y, w, h a adapter
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    return frame
    #----------USEFULL FOR DEBUG
    
    #cv2.imshow("frame", frame)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    



def treatment_nvgris(seuil,img):
    seuil_gris=seuil
    #img = cv2.imread('map5.jpg',0)
    
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(img,-1,kernel)
    
    #cv2.imshow('smotthing2',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    height = np.size(dst, 0)
    width = np.size(dst, 1)
    #print(height,width)
    
    
    for x in range (width-1):
     for y in range (height-1):
         px = dst[y,x]
         if px>seuil_gris:
             dst[y,x]=255
    
    cv2.imshow('smotthing2',dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return dst
    



def treatment_localisation(frame,thresdown,threshold):
    Found=[]
    somme=0
    compteur=0
    for x in range (0,780,20):   #800, par pas de 20      noyaux de 40 par 130 
        for y in range (0,408,17):
            somme=0
            
            compteur=compteur+1
            
            
            for x_current in range (x,x+40,1):
                for y_current in range (y,130+y,1):
                    poid=frame[y_current,x_current]
                    somme=somme+poid
                    
            if thresdown<somme<threshold:
                #print("Arbre trouve numero sur la boucle ",x)
                #print ("COMPTEUR =",compteur )
                #print("somme =",somme)

                pos_arbre_x=x+20
                pos_arbre_y=y+65
                
                Found.append(pos_arbre_x)
                Found.append(pos_arbre_y)

    return Found




def display_Found(image,liste):
    
    size=len(liste)
    
    for i in range(0,size,2):
        x_value=liste[i]
        y_value=liste[i+1]
        
        image[y_value,x_value]=[0,0,255]
        image[y_value+1,x_value+1]=[0,0,255]
        image[y_value-1,x_value-1]=[0,0,255]
        image[y_value-1,x_value]=[0,0,255]
        image[y_value+1,x_value]=[0,0,255]
        image[y_value,x_value+1]=[0,0,255]
        image[y_value,x_value-1]=[0,0,255]
        image[y_value-1,x_value+1]=[0,0,255]
        image[y_value+1,x_value-1]=[0,0,255]
        
    cv2.imshow('smotthing2',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    