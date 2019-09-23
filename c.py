import os
from requests import get
import time

##set
host = '192.168.43.160'
num = 1
##
g = ''

while str(num) != g:
	time.sleep(0.1)
	g = get('http://' + host + '/gt').text
	#print(g)
os.system('sl')
get('http://' + host + '/sw')