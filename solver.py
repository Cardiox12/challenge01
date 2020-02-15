from string import ascii_lowercase
import time

FILE_PREFIX = "letters"

# Colors
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def get_ascii_letter(letter):
	if letter in ascii_lowercase:
		with open(f"{FILE_PREFIX}/{letter}", "r") as f:
			return f.readlines()
	return None

def get_letter(ascii_art_letter):
	# Your code here
	pass

def test_challenge01():
	counter = 0
	begin = time.time()
	# Testing time
	for letter in ascii_lowercase:
		get_letter(get_ascii_letter(letter))
	end_time = time.time() - begin

	# Testing correct answer
	for letter in ascii_lowercase:
		if letter == get_letter(get_ascii_letter(letter)):
			counter += 1
			print(f"{letter} -> [{OKGREEN}✓{ENDC}]")
		else:
			print(f"{letter} -> [{FAIL}x{ENDC}]")

	print(f"Total : {counter} / {len(ascii_lowercase)}")
	print(f"Executed in : {end_time:.5f}s")


test_challenge01()