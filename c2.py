import os
from requests import get
from time import sleep as s

##set
host = '192.168.43.160'
num = 1

speed = 16

rows, col = os.popen('stty size','r').read().split()
deelay = int(col) / speed

##
g = ''

while str(num) != g:
        s(0.1)
        g = get('http://' + host + '/gt').text
        #print(g)

s(delay)
get('http://'+host+'/sw')
os.system('sl')