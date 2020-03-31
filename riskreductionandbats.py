a=open('rred.txt','r')
a=a.read()
a=a.split('\n')
b=[]
for x in a:
    b.append(x.split(" "))
#print(b[0][1],int(b[0][2]))

c=sorted(b,key=lambda x: int(x[1]))
for x in c:
    print (x[1],'  ',x[2],'    ',x[0])
import keyboard  # using module keyboard
import time
import win32api, win32con
import clipboard
import winsound
import datetime
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return [ pt.x,  pt.y]


count=0
i=[]
p=[]
import random
#--crimesarray
crimesarraycoordinates=open("coordinates.txt","r")
crimesarraycoordinates=crimesarraycoordinates.read()
crimesarraycoordinates=crimesarraycoordinates.split('\n')
fil1=[k.split(" ") for k in crimesarraycoordinates]
for x in range(len(crimesarraycoordinates)):
    crimesarraycoordinates[x]=[int(fil1[x][0]),int(fil1[x][1]),int(fil1[x][2]),int(fil1[x][3])]
#print(crimesarraycoordinates)
moneyc=open("cmoney.txt","r")
moneyc=moneyc.read()
moneyc=moneyc.split('\n')
fil1=[k.split(" ") for k in moneyc]
for x in range(len(moneyc)):
    moneyc[x]=[int(fil1[x][0]),int(fil1[x][1]),int(fil1[x][2]),int(fil1[x][3])]

class c_index:
    def __init__(self,list):
        self.list=list
        self.index=0
    def increase(self):
        if(self.index==len(self.list)-1):
            self.index=0
            winsound.Beep(frequency, duration)
        else:
            self.index+=1
    def access(self):
        click(self.list[self.index][0],self.list[self.index][1])
        time.sleep(0.2)
        click(self.list[self.index][2],self.list[self.index][3])
        self.increase()
reducerisk=c_index(crimesarraycoordinates)
new_money=c_index(moneyc)
print(reducerisk.list," ",len(reducerisk.list))
# time.sleep(5)
# click(int(fil1[0][0]),int(fil1[0][1]))
# time.sleep(0.2)
# click(int(fil1[0][2]),int(fil1[0][3]))

#-------testing and pinging mouse points
# while True:
	# # making a loop # used try so that if user pressed other than the given key error will not be shown
    # if keyboard.is_pressed('i'):
        # i=queryMousePosition()
        # print('image recieved',count)
        # time.sleep(0.2)  
    # if keyboard.is_pressed('p'):
        # p=queryMousePosition()
        # print('prestuplenie position recieved',count)
        # time.sleep(0.2)
    # if keyboard.is_pressed('l'):
        # text=clipboard.paste()
        # b=open('coordinatesn.txt','a')
        # k=str(i[0])+" "+str(i[1])+" "+str(p[0])+" "+str(p[1])+" "+text+"\n"
        # print(text, ' added')
        # b.write(k)
        # time.sleep(0.2)
        # b.close()
    # if keyboard.is_pressed('j'):
        # break
    # if keyboard.is_pressed('t'):
        # click(i[0],i[1])
        # time.sleep(0.2)
    # if keyboard.is_pressed('r'):
        # click(p[0],p[1])
        # time.sleep(0.2)
s=str
money=False
while True:
	# # making a loop # used try so that if user pressed other than the given key error will not be shown
    if(money):
        if keyboard.is_pressed('k'):
            click(749,585 )
            time.sleep(0.2)
            click(775 ,613)
            time.sleep(0.2)
        if keyboard.is_pressed('o'):
            click(678 ,642  )
            time.sleep(0.2)
            click(693  ,670)
            time.sleep(0.2)
        if keyboard.is_pressed('l'):
        #1142 262 1142 262 http://bgmafia.com/map/5~1/shaft.move?z=hHs#

            click(1142,262)
            time.sleep(0.2)
        if keyboard.is_pressed('m'):
            money=False
            
            print(False)
            time.sleep(0.2)
    else:
        # if keyboard.is_pressed('c'):
            # click(796,458)
            # time.sleep(0.1)
            # click(815,540)
            # time.sleep(0.1)
        if keyboard.is_pressed('k'):
            # print("yayy")
            reducerisk.access()
            time.sleep(0.4)
            # #920,344
            # click(920,344)
            # #1072 263
        
        if keyboard.is_pressed('h'):
            # print("yayy")
            new_money.access()
            time.sleep(0.4)
        if keyboard.is_pressed('l'):
        #1142 262 1142 262 http://bgmafia.com/map/5~1/shaft.move?z=hHs#

            click(1071, 266)
            time.sleep(0.2)
        if keyboard.is_pressed('n'):
            # print("yayy")
            now = datetime.datetime.now()
            file=open('beaten.txt','a')
            text="\n"+clipboard.paste().strip()+"<>"+s(now.hour)+":"+s(now.minute)
            try:
                file.write(text)
            except:
                time.sleep(0.2)
            print(text," added")
            time.sleep(0.4)
            # #920,344
            # click(920,344)
            # #1072 263
        if keyboard.is_pressed('x'):
            text=clipboard.paste().strip()
            with open('beaten.txt') as f:
                if text in f.read():
                    winsound.Beep(frequency, duration)
            time.sleep(0.2)
        if keyboard.is_pressed('m'):
            money=True
            print(True)
            time.sleep(0.2)
        if keyboard.is_pressed('j'):
            break
    time.sleep(0.01)