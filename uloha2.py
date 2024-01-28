from decimal import *

try:
  print("Bod A:")
  bod1 = input()
  (x1, y1) = bod1.split(" ", 2)
  x1 = float(x1)
  y1 = float(y1)

  print("Bod B:")
  bod2 = input()
  (x2, y2) = bod2.split(" ", 2)
  x2 = float(x2)
  y2 = float(y2)
    
  print("Bod C:")
  bod3 = input()
  (x3, y3) = bod3.split(" ", 2)
  x3 = float(x3)
  y3 = float(y3)

  if (x1==x2 and y1==y2 or x2==x3 and y2==y3 or x1==x3 and y1==y3):
    print("Nektere body splyvaji.")
  else:
    # plocha trojuhelnika je nula pokud jsou v primce
    p = round((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)),3)
    
    if (p == 0):   
      print ("Body lezi na jedne primce.")  
      xmin = min (x1, x2, x3)
      xmax = max (x1, x2, x3)
      if (xmin != xmax):
        if (x1 > xmin and x1 < xmax):
          print ("Prostredni je bod A.")  
        if (x2 > xmin and x2 < xmax):
          print ("Prostredni je bod B.")  
        if (x3 > xmin and x3 < xmax):
          print ("Prostredni je bod C.")  
      else:    
        ymin = min (y1, y2, y3)
        ymax = max (y1, y2, y3)
        if (y1 > ymin and y1 < ymax):
          print ("Prostredni je bod A.")  
        if (y2 > ymin and y2 < ymax):
          print ("Prostredni je bod B.")  
        if (y3 > ymin and y3 < ymax):
          print ("Prostredni je bod C.")  
        
    else:  
      print ("Body nelezi na jedne primce.")  

except:
  print("Nespravny vstup.")
  exit