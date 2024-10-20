"""The function takes a number and a range (low and high values) and tries to guess a number using binary search.
    Returns the guessed number and the number of attempts, which were required for the search. If the number is not found in the range, returns None and the number of attempts.
    Guessing arguments:
    number (int): The number that needs to be guessed.
    low (int): The lower limit of the search range.
    high (int): The upper limit of the search range.
The program displays the desired number and the number of attempts
"""


def guessing(number, low, high):
    attempts = 0
    while low <= high:
        attempts += 1
        middle = (low + high) // 2

        if middle < number:
            low = middle + 1
        elif middle > number:
            high = middle
        else:
            return middle, attempts

    return None, attempts


target_number = int(input("Guess the number from 1 to 100: "))

while target_number < 1 or target_number > 100:
    print("Guess the number from 1 to 100.")
    target_number = int(input("Guess the number from 1 to 100: "))

guessed_number, num_attempts = guessing(target_number, 1, 100)

if guessed_number is not None:
    print(f"I guessed your number: {guessed_number} in {num_attempts} attempts!")
else:
    print("Couldn't guess the number.")
