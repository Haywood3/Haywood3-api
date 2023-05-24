import random
import string
# generate strong randomized passwords
word_length = 33
# generate a list of letters, digits, and some punctuation
components = [string.ascii_letters, string.digits, "!@#$%&"]

char = []

for component in components:
	for item in component:
		char.append(item)
def generate_password():
	# store the password
	password = []
	# choose a random item from chars and add it to password
	for i in range(word_length):
		randomchar = random.choice(char)
		password.append(randomchar)
	# return password as a string
	return "".join(password)
print(generate_password())