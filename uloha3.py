# preveden cislo num na retezec cisla o zakladu b
def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
  return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

# je rezec palindrom ?
def isPalindrome(s):
  return s == s[::-1]

# urci dalsi palindrom od cisla n pri zakladu radix
# vraci (uspech, next, next_string_pro_kontrolu)
def nextPalindrome (n, radix):
  try:
    radix = int(radix)
  except:
    return (0, 0, "")
    
  if (radix > 36):
    return (0, 0, "")
  
  n1 = n
  n1str = baseN(n, radix)
  while(not isPalindrome(n1str)):
    n1 += 1
    n1str = baseN(n1, radix)
    #print(n1, n1str)

  next = n1
  return (1, n1, n1str)
  
print (nextPalindrome(14781, 7))