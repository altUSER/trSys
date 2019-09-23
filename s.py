from bottle import *

n = 0

@route('/sw')
def sw():
	global n
	n+=1
	print(n)

@route('/gt')
def gt():
	global n
	return(str(n))

run(host='localhost', port=80)