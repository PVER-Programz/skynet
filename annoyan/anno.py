# Anno.py

import pyautogui
import time
import os

process_id = os.getpid()
Xmax, Ymax = pyautogui.size()
pver_safe=0

with open("pid.pver", 'w') as f:
	f.write(str(process_id))

print("Begin")
while True:
	x, y = 0, 0
	Xcur, Ycur = pyautogui.position()
	if Xcur % 2 == 0 :
		x=0-(Xcur//2)
	else:
		x=(Xmax-Xcur)//2
	if Ycur % 2 == 0 :
		y=0-(Ycur//2)
	else:
		y=(Ymax-Ycur)//2
	if str(int(time.time()))[-1]=='0':
		movetime = 0.5
	else:
		movetime = int(str(int(time.time()))[-1])
	waitime = time.localtime().tm_sec
	# waitime, movetime = 1, 1
	print("Moving", x, y, "for", movetime)
	try:
		pyautogui.move(x, y, movetime)
		print("Sleeping", waitime)
		time.sleep(waitime)
	except pyautogui.FailSafeException:
		print("Thrown")
		pver_safe=pver_safe+1
		if pver_safe>=4:
			time.sleep(pver_safe*10)
		else:
			time.sleep(1)
			continue
