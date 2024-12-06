import os
try:
	import psutil
except:
	os.system("py -m pip install psutil")
import time

while True:
	try:
		with open("pid.pver", "r") as f:
			pid_to_check = int(f.read())
	except FileNotFoundError:
		print("No file")
		pid_to_check = 6942069
	if psutil.pid_exists(pid_to_check):
		print(f"Process {pid_to_check} is running.")
	else:
		print(f"Process {pid_to_check} is not running.")
		os.system("start py anno.py")
	time.sleep(20)
