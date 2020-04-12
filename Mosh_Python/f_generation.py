for line in range(4):
	if int(line)%2 == 0:
		for column_even in range(5):
			print("X", end = "")
		print("")
	else:
		for column_odd in range(2):
			print("X", end = "")
		print("")
print("XX")
print("")

patten = [2, 2, 2, 2, 5]
for x_cont in patten:
	for x_num in range(int(x_cont)):
		print("X", end = "")
	print("") 
