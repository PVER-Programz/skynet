import sys
import time
import pyautogui as p
import math

def flash(string):
	sys.stdout.write(string)
	sys.stdout.flush()
	sys.stdout.write(" "*len(string))
	sys.stdout.write("\b"*3*len(string))
	# sys.stdout.flush()

def res(x, y):
	return math.sqrt((x**2)+(y**2))

while 1:
	Xi, Yi = p.position()
	Ti = time.time()
	time.sleep(0.01)
	Xf, Yf = p.position()
	Tf = time.time()
	DelX = Xf-Xi
	DelY = Yf-Yi
	DelT= Tf-Ti
	sult = res(DelX,DelY)
	if DelX/DelT!=0.0 and DelY/DelT!=0:
		print(f"x: {DelX/DelT} px/sec \t y:{DelY/DelT} px/sec \t r:{sult/DelT} px/sec")
