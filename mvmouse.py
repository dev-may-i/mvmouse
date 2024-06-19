#! python3
import pyautogui, sys
import random
import time

t = 10

print('Press Ctrl-C to quit.')

def timeFlux():
  global t
  t_flux = random.randint(-9,9)
  tf = t + t_flux
  if (tf) < 0:
    tf = t
  print("\nt: " + str(t) + " flux: " + str(t_flux) + " new: " + str(tf) )
  return(tf)

def getCursorPosition():
   x, y = pyautogui.position()
   positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
   print(positionStr, end='')
   print('\b' * len(positionStr), end='', flush=True)
   return(x,y)
   
def getRanNum():
   rnd_x = random.randint(0,9)
   rnd_y = random.randint(0,9)
   return(rnd_x,rnd_y)
   
def mvCursor(x,y):
   print("New Position: " + str(x), str(y) )
   pyautogui.moveTo(int(x), int(y)) 
    
try:
  while True:
    x,y = getCursorPosition()
    rnd_x,rnd_y = getRanNum()
    x_max, y_max = pyautogui.size()
    
    if (x + rnd_x) < (x_max - 10):
        x = x + rnd_x
    else:
        x = x - rnd_x
    
    if (y + rnd_y) < (y_max - 10):
        y = y + rnd_y
    else:
        y = y - rnd_y
    
    mvCursor(x,y)
    tf = timeFlux()
    time.sleep(tf)
except KeyboardInterrupt:
    print('\n')
