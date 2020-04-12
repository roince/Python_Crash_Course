numbers =  [11, 3, 23, 63, 233, 11, 23, 33, 33, 33, 23, 23, 11, 233]

# solution 1: literally remove the duplicates from the numbers list
""" for number in numbers:
	number_count = numbers.count(number)
	if (number_count > 1):
		for count in range(number_count-1):
			numbers.remove(number) """

# solution 2: Mosh's solution: add unique numbers into the 2nd list --> way easier
uniques = []
for number in numbers:
	if number not in uniques:
		uniques.append(number)

print (uniques)
# print (set(numbers))