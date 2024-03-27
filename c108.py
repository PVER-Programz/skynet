import time

tryfor = 0.5
repeatfor = 5

def getavg(lis):
	a = 0
	for x in lis:
		a=a+x
	return a/len(lis)

start = time.time()
print("start time: ", start)
gaps = [tryfor]
for x in range(repeatfor):
	print('\n--------------')
	now = time.time()
	print("Now: ", now)
	expect = getavg(gaps)
	print("Expect: ", expect)
	# input("PRESS")
	time.sleep(tryfor)
	gap = time.time()-now
	print("Gap: ", gap)
	print("Diff: ", abs(gap - expect))
	gaps.append(gap)
	print("--------------\n")

print("Final Real: ", gaps[-1])
print("Final Expect: ", getavg(gaps))
print("Final Diff: ", abs(gaps[-1]-getavg(gaps)))