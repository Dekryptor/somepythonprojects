import keyboard  # using module keyboard
import time
import win32api, win32con
import winsound
from ctypes import windll, Structure, c_long, byref
def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    

def point1(x,y):
    win32api.SetCursorPos((x,y))
    
    
def hover(x,y,x1,y1):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(0.1)
    win32api.SetCursorPos((x1,y1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x1,y1,0,0)
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def hamburger_create():
    click(475 ,784)#bunsadded
    time.sleep(0.1)
    hover(957 ,737 ,463, 665)
    time.sleep(0.1)
    
    
def hamburger_add_marulq():
    hover(765, 611 ,463, 665)
    time.sleep(0.1)
    
    
def hamburger_add_tomato():
    hover(786,715 ,463, 665)
    time.sleep(0.1)
    
def hamburger_with_marulq():
    hamburger_create()
    hamburger_add_marulq()
    
 
def hamburger_with_tomato():
    hamburger_create()
    hamburger_add_tomato()
    
    
def hamburger_with_tomato_marulq():
    hamburger_create()
    hamburger_add_tomato()
    hamburger_add_marulq()
    

def hb_point():
    point1(463, 665)
    time.sleep(0.1)
    

def hotdog_create():
    click(647, 778)#bunsadded
    time.sleep(0.1)
    hover(1082, 724 ,635,656)
    time.sleep(0.1)
    

def hotdog_add_ketchup():
    hover(761, 487 ,635,656)
    time.sleep(0.1)
    

def hotdog_with_ketchup():
    hotdog_create()
    hotdog_add_ketchup()
    time.sleep(0.1)
    
    
def hd_point():
    point1(635 , 656 )
    time.sleep(0.1)
    


def fries_fri():
    click(311, 792)#bunsadded
    time.sleep(0.1)
    
class fries_c:
    def __init__(self):
        self.list=[389, 493],[361, 564],[333, 648]
        self.index=0
    def increase(self):
        if(self.index==len(self.list)-1):
            self.index=0
        else:
            self.index+=1
    def access(self):
        point1(self.list[self.index][0],self.list[self.index][1])
        time.sleep(0.1)
        self.increase()
        
        
class cola_c:
    def __init__(self):
        self.list=[236 , 648 ],[170 , 649 ],[102 , 639]
        self.index=0
    def increase(self):
        if(self.index==len(self.list)-1):
            self.index=0
        else:
            self.index+=1
    def access(self):
        point1(self.list[self.index][0],self.list[self.index][1])
        time.sleep(0.1)
        self.increase()
        
        
def deliver(c):
    mp=queryMousePosition()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,mp[0],mp[1],0,0)
    time.sleep(0.1)
    win32api.SetCursorPos((c[0],c[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,c[0],c[1],0,0)
    time.sleep(0.1)
    

def collectmoney():
    m=[236,415],[538,423],[837,414],[1154,421]
    for x in range(4):
        click(m[x][0],m[x][1])
        time.sleep(0.05)
        

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return [ pt.x,  pt.y]
i=[]
p=[]
fries=fries_c()
cola=cola_c()
c_1= [238, 337]
c_2= [534 , 311 ]
c_3= [865 , 327 ]
c_4= [1187 , 325]
#keys 4 - hamburger 5 - hamburger_marulq 6- hamburger_tomato + - hmt
#1 hotdog 2 hotdog ketchup
#c1 - 7 - hb, 8-hd, 9-fries, 0 - cola
#c2 - u - hb, i-hd, o-fries, p - cola
#c3 - j - hb, k-hd, l-fries, ; - cola
#c4 - m - hb, ,-hd, .-fries, / - cola
while True:
	# making a loop # used try so that if user pressed other than the given key error will not be shown
    # if keyboard.is_pressed('i'):
    if keyboard.is_pressed('4'):
        hamburger_create()
    if keyboard.is_pressed('5'):
        hamburger_with_marulq()
    if keyboard.is_pressed('6'):
        hamburger_with_tomato()
    if keyboard.is_pressed('+'):
        hamburger_with_tomato_marulq()
    if keyboard.is_pressed('1'):
        hotdog_create()
    if keyboard.is_pressed('2'):
        hotdog_with_ketchup()
    if keyboard.is_pressed('r'):
        cola.access()
        deliver(c_1)
    if keyboard.is_pressed('t'):
        cola.access()
        deliver(c_2)
    if keyboard.is_pressed('y'):
        cola.access()
        deliver(c_3)
    if keyboard.is_pressed('u'):
        cola.access()
        deliver(c_4)
    if keyboard.is_pressed('f'):
        fries.access()
        deliver(c_1)
    if keyboard.is_pressed('g'):
        fries.access()
        deliver(c_2)
    if keyboard.is_pressed('h'):
        fries.access()
        deliver(c_3)
    if keyboard.is_pressed('j'):
        fries.access()
        deliver(c_4)
    
    if keyboard.is_pressed('c'):
        collectmoney()
    if keyboard.is_pressed('a'):
        fries_fri()
    # if keyboard.is_pressed('i'):
        # i=queryMousePosition()
        # print('image recieved', i)
        # time.sleep(0.2)  
    # if keyboard.is_pressed('l'):
        # b=open('coordinatesn.txt','a')
        # k=str(i[0])+" "+str(i[1])+"\n"
        # b.write(k)
        # time.sleep(0.2)
        # b.close()
    
    if keyboard.is_pressed('x'):
        break
    # if keyboard.is_pressed('k'):
        # fries.access()
        # time.sleep(0.2)
    # if keyboard.is_pressed('r'):
        # point1(i[0],i[1])
        # #click(311, 792)
        # time.sleep(0.2)
        
    time.sleep(0.01)