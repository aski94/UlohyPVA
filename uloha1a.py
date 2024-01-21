
import math

try:
  print("Rozmer mistnosti:")
  hrana = int(input())

  print("Bod #1:")
  bod1 = input()
  (x1, y1, z1) = bod1.split(" ", 3)
  x1 = int(x1)
  y1 = int(y1)
  z1 = int(z1)
  if (x1!=0 and x1!=hrana and (x1<20 or x1>hrana-20)):
    raise Exception
  if (y1!=0 and y1!=hrana and (y1<20 or y1>hrana-20)):
    raise Exception
  if (z1!=0 and z1!=hrana and (z1<20 or z1>hrana-20)):
    raise Exception
    
  print("Bod #2:")
  bod2 = input()
  (x2, y2, z2) = bod2.split(" ", 3)
  x2 = int(x2)
  y2 = int(y2)
  z2 = int(z2)
  if (x2!=0 and x2!=hrana and (x2<20 or x2>hrana-20)):
    raise Exception
  if (y2!=0 and y2!=hrana and (y2<20 or y2>hrana-20)):
    raise Exception
  if (z2!=0 and z2!=hrana and (z2<20 or z2>hrana-20)):
    raise Exception

  potrubi = 0
  hadice = 0
  
  # geometricka vzdalenost bodu
  xclen = abs(x1-x2)   
  yclen = abs(y1-y2)
  zclen = abs(z1-z2)

  # sousedni hrany
  potrubi = xclen + yclen + zclen
  if (x1!=0 and x1!=hrana and x2!=0 and x2!=hrana):
    hadice = math.sqrt((zclen+yclen)**2 + (xclen)**2)
  if (y1!=0 and y1!=hrana and y2!=0 and y2!=hrana):
    hadice = math.sqrt((zclen+xclen)**2 + (yclen)**2)
  if (z1!=0 and z1!=hrana and z2!=0 and z2!=hrana):
    hadice = math.sqrt((yclen+xclen)**2 + (zclen)**2)

  # protilehle pripad z
  if (zclen==hrana):
    xclen2  = min(hrana-x1+hrana-x2, x1 + x2)    
    yclen2  = min(hrana-y1+hrana-y2, y1 + y2)    
    potrubi = min(xclen2 + yclen + zclen, xclen + yclen2 + zclen)
    hadice  = min(math.sqrt((xclen2 + zclen)**2 + yclen**2), math.sqrt((yclen2 + zclen)**2 + xclen**2))

  # protilehle pripad y
  if (yclen==hrana):
    xclen2  = min(hrana-x1+hrana-x2, x1 + x2)    
    zclen2  = min(hrana-z1+hrana-z2, z1 + z2)    
    potrubi = min(xclen2 + yclen + zclen, xclen + yclen + zclen2)
    hadice  = min(math.sqrt((xclen2 + yclen)**2 + zclen**2), math.sqrt((zclen2 + yclen)**2 + xclen**2))

  # protilehle pripad x
  if (xclen==hrana):
    yclen2  = min(hrana-y1+hrana-y2, y1 + y2)    
    zclen2  = min(hrana-z1+hrana-z2, z1 + z2)    
    potrubi = min(xclen + yclen2 + zclen, xclen + yclen + zclen2)
    hadice  = min(math.sqrt((yclen2 + xclen)**2 + zclen**2), math.sqrt((zclen2 + xclen)**2 + yclen**2))

  print("Delka potrubi: {}".format(potrubi))
  print("Delka hadice: {}".format(hadice))

except:
  print("Nespravny vstup.")
  exit
  
