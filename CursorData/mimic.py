import sys
import os
import time
import pyautogui as p
import math

loadT = time.time()
Ts=[0]
T2s=[0]
X, Y = p.position()
Xs = [X]
Ys = [Y]

while 1:
	try:
		if p.position() != (X,Y):
			X, Y = p.position()
			T = time.time()-loadT
			T2=T-Ts[-1]
			Ts.append(T)
			T2s.append(T2)
			Xs.append(X)
			Ys.append(Y)
			print(f"x: {X} y:{Y} t:{T} t2:{T2}")
			time.sleep(0.1)
	except KeyboardInterrupt:
		print("\n")
		print("X: ", len(Xs))
		print("Y: ", len(Ys))
		print("T: ", len(Ts))
		print("T2: ", len(T2s))
		print("\n")
		# for x in Ts:
		# 	print(x)
		# print("\n")
		# for x in T2s:
		# 	print(x)
		break

input("-- Code Break--\n")
# os.system("cls")

Xs.pop(0)
Ys.pop(0)
Ts.pop(0)
T2s.pop(0)
curdata=[]
for i in range(len(Ts)):
	curdata.append({'x': Xs[i], 'y': Ys[i], 't': Ts[i], 't2': T2s[i]})
	print({'x': Xs[i], 'y': Ys[i], 't': Ts[i], 't2': T2s[i]})

pwd = input("\n\nClearance Code: ")

if pwd != "4444":
	print("Aborted")
	exit()

trialtime_i = time.time()
for i in curdata:
	p.moveTo(i['x'], i['y'], i['t2'])
trialtime_f = time.time()

Deltrialtime = trialtime_f - trialtime_i
print(f'\nTrial Time: {Deltrialtime}')
supptime=sum(T2s)
print(f"Supposed Time: {supptime}")
print(f"Time Diff: {abs(supptime- Deltrialtime)}")