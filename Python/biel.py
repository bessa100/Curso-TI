import random
import string

LETTERS  = string.ascii_letters
NUMS ='0123456789'
SPE = '-+*%&$!_'
SYMBOLS = LETTERS + NUMS + SPE 
p = ''
len = int(input("ENTER PASS.LENGTH:"))
password = p.join(random.sample(SYMBOLS, len))

print(password)