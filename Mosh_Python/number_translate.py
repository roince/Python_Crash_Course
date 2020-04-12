number_word = {
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
	"5": "five",
	"6": "six",
	"7": "seven",
	"8": "eight",
	"9": "nine",
	"0": "zero"
}

phone_number = input("phone number: ")
if phone_number.isdigit():
	for digit in phone_number:
		print(number_word[digit].title() + " ", end = "")
	print("")
else:
	print("please enter only digit as phone numbers!")
