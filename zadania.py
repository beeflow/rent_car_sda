# create a function which will return phone number prepared from a list of 10 digits in format
# (123) 123-1234

# print( create_phone_number( [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] ) )
def create_phone_number(n: list) -> str:
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# exercise 2
# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# Take this opportunity to practice using functions.

def is_prime(n: int) -> bool:
    return len([x for x in range(2, int(n ** 0.5) + 1) if n % x == 0]) == 0 and n != 1

# exercise 4
# Write a program (using functions!) that asks the user for a long string containing
# multiple words. Print back to the user the same string, except with the words
# in backwards order. For example, say I type the string:
#
#   My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me.

def inverse_sentence(sentence: str) -> str:
    return ' '.join(sentence.split(' ')[::-1])


# exercise 5
# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
# (8x8 for chess, 19x19 for Go, and many more).
#
# Ask the user what size game board they want to draw, and draw it for them to the screen
# using Python’s print statement.

def draw_game_board(x: int):
    return x * (' ---' * x + '\n' + '|   ' * x + '|\n') + ' ---' * x
