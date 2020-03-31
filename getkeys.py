import keyboard  # using module keyboard
import time
import win32api, win32con
import clipboard
import winsound
from ctypes import windll, Structure, c_long, byref
def click(x,y):
    win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return [ pt.x,  pt.y]
i=[]
p=[]
while True:
	# making a loop # used try so that if user pressed other than the given key error will not be shown
    if keyboard.is_pressed('i'):
        i=queryMousePosition()
        print('image recieved', i)
        time.sleep(0.2)  
    if keyboard.is_pressed('p'):
        p=queryMousePosition()
        print('prestuplenie position recieved')
        time.sleep(0.2)
    if keyboard.is_pressed('l'):
        text=clipboard.paste()
        b=open('coordinatesn.txt','a')
        k=str(i[0])+" "+str(i[1])+" "+str(p[0])+" "+str(p[1])+"\n"
        print(text, ' added')
        b.write(k)
        time.sleep(0.2)
        b.close()
    if keyboard.is_pressed('j'):
        break
    if keyboard.is_pressed('t'):
        click(p[0],p[1])
        time.sleep(0.2)
    if keyboard.is_pressed('r'):
        click(i[0],i[1])
        time.sleep(0.2)
        
    time.sleep(0.01)