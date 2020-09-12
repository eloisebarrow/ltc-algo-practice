#Given a two-digit integer, return the sum of its digits.


def sum_digits(two_digit_number):


	two_digit_number_as_string = str(two_digit_number)


	first_char = two_digit_number_as_string[:1]


	second_char = two_digit_number_as_string[-1]


	first_char_as_int = int(first_char)


	second_char_as_int = int(second_char)


	addition = first_char_as_int + second_char_as_int



	print("two digit number is:")
	print(two_digit_number)
	print("sum is:")
	print(addition)


sum_digits(32)
