import os
from requests import get
import time

##set
host = 'localhost'
num = 1
##
g = ''

while str(num) != g:
	time.sleep(0.1)
	g = get('http://' + host + '/gt').text
	#print(g)
os.system('sl')
get('http://' + host + '/sw')