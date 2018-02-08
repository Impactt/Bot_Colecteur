import win32api, win32con, time, random

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    

tempon_x,tempon_y = win32api.GetCursorPos()
compteur=0

while 1 :
     time.sleep(1)
     h_x, h_y = win32api.GetCursorPos()
     
     if tempon_x == h_x and tempon_y == h_y:
         compteur=compteur+1
         
     else:
         compteur=0
     
     tempon_x=h_x
     tempon_y=h_y
     
     print(h_x,h_y)
     
     if compteur>300:
         click(1433,1026) #premier c'est horizontal
         time.sleep(1+random.random()) #nike le bot
         click(1433,1030)
         print("reset le tout")
         compteur=0



    





















