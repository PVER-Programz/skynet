import random
import time

strt = time.time()
opt = [1,2,3,4,5,6,7,8,9,0]
key = [4, 1, 2, 4, 4, 2, 2, 4, 3, 2,
	2, 3, 4, 4, 2, 1, 4, 2, 3, 1,
	1, 1, 1, 1, 1, 2, 4, 3, 1, 1,
	1, 2, 4, 2, 1, 1, 1, 2, 3, 2,
	4, 4, 2, 2, 3, 3, 1, 4, 1, 4]
alt_key = [1,2,3,4,5,6]
loop_total = 10000
best = {"Loop Number": 0, "Trues": 0}
q_count=6

key = alt_key

for loop_number in range(loop_total):
	gen = []
	comp = []
	ones = 0
	zero = 0

	for x in range(q_count):
		gen.append(random.choice(opt))

	for y in range(q_count):
		if gen[y]==key[y]:
			comp.append(1)
			ones = ones+1
		else:
			comp.append(0)
			zero = zero+1

	if ones > best["Trues"]:
		best["Trues"] = ones
		best["Loop Number"] = loop_number+1
		best["False"] = zero

	print("____________________________\n")
	print("Loop: ", loop_number+1)
	print("Match: ", gen==key)
	print("Gen: ",gen)
	print("Com: ", comp)
	print("Ones: ", ones)
	print("Zeroes: ", zero)

	if gen==key:
		result="Positive"
		break
	else:
		result="Negative"

print("\n\n<================================>\n")
print("Result: ",result)
print("Looped: ", loop_total)
print("Key: " ,key)
print("Best: ", best)
print("Run time:", time.time() - strt, "Seconds")