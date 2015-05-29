def find(substring, string):

	#Preprocessing
	bad_char = get_char_table(substring)

	#Assuming match is false
	matched = False
	current_index = len(substring) - 1

	matched = matches(substring, string, current_index)

	end_reached = False

	success = True

	while matched != True and success == True:

		#Find shift

		if matched in bad_char:
			shift = bad_char[matched]
		else:
			shift = bad_char['*']

		#Adjust index
		current_index += shift

		if current_index > len(string) - 1:
			current_index = len(string) - 1
			end_reached = True
			success = False

		#Update matched
		matched = matches(substring, string, current_index)

	if success:
		return current_index - (len(substring) -1)
	else:
		return False

def get_char_table(substring):

	unique_chars = {}

	index = 0

	for char in substring:
		unique_chars[char] = max(1, len(substring) - 1 - index)
		index += 1

	last_char = substring[-1]

	if substring.count(last_char) == 1:
		unique_chars[last_char] = len(substring)

	unique_chars['*'] = len(substring)

	return unique_chars

def matches(substring, string, index):

	inverted_sub = substring[::-1]
	first_char = string[index]

	for char in inverted_sub:

		string_char = string[index]


		if char != string_char:
			return first_char

		index = index -1


	return True