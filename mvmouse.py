#! python3
import pyautogui, sys
import random
import time


t = 10
x_max, y_max = pyautogui.size()

pyautogui.FAILSAFE = False   # The script will not move the mouse-pointe into the FAILSAFE zone, but the user may. 
                             # To prevent the app from crashing the FAILSAFE will be disabled.
                             # Since a timer is in place there should be no problems interrupting the process
                             
x_max_d = x_max - 10         # Shrink the action window to prevent running into FAILSAFE exception
y_max_d = y_max - 10

print('Press Ctrl-C to quit.')

def timeFlux():
  global t
  t_flux = random.randint(-9,9)
  tf = t + t_flux
  if (tf) < 0:
    tf = t
  # print("\nt: " + str(t) + " flux: " + str(t_flux) + " new: " + str(tf) )
  return(tf)

def getCursorPosition():
   x, y = pyautogui.position()
   return(x,y)
   
def getRanNum():
  rnd_x = random.randint(0,9)
  rnd_y = random.randint(0,9)
  return(rnd_x,rnd_y)
   
def mvCursor(x,y):
  pyautogui.moveTo(int(x), int(y) )   
    
try:
  while True:
    x,y = getCursorPosition()
    rnd_x,rnd_y = getRanNum()
    tf = timeFlux()
    
    if (x + rnd_x) < x_max_d:
        x = x + rnd_x
    else:
        x = x - rnd_x
    
    if (y + rnd_y) < y_max_d:
        y = y + rnd_y
    else:
        y = y - rnd_y
    
    #mvCursor(x,y) 
    pyautogui.moveTo(x,y)
    x,y =  getCursorPosition()
    positionStr = "t: " + str(tf) + " X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)
    time.sleep(tf)
except KeyboardInterrupt:
    print('\n')
