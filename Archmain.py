#CTRL 4 pour commenter
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
import fonctions


min =1 
max= 4    
porte = 0


while porte < min or porte > max:  
    porte=int(input("valeur de range entre 1 et 4 ?   "))
    print( porte ) 
    
pos_x= porte
pos_y= porte

actualx=pos_x
actualy=pos_y

compteur=0
edge=porte*2      #(en 2:2) par exemple2

while 1 :
   
    #==========On bouge======================
    for i in range (200):

        (actualy,actualx,direction)=decision(pos_x,pos_y)
            
        if actualx >= 0 and actualx <= edge and actualy >= 0 and actualy <= edge :  #valide la condition
            break    
    
    pos_x=actualx
    pos_y=actualy      
             
    time_wait=random.randint(1,10)*0.1
    time.sleep(time_wait)

    directions(direction)

    print("numero du tour =",compteur)
    

    
    air=interupt(20)  #F2 to stop the program, x0.1 so 2 second here
    if air==False:
        print("END")
        break
        
    frame=capture_frame()
    first_outpout=treatment_nvgris(110,frame)

    thresdown=1050000
    threshold=1200000
    
    value=treatment_localisation(first_outpout,thresdown,threshold)
    #display_Found(second,value)

    if compteur==20:
        print("END")
        break
    else :
        compteur=compteur+1
    
