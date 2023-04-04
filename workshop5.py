# Bonus tasks 1-3 completed


import random

# Task 1
# Added bonus task 1. Also added validation that user cannot enter anything but a valid number.
# Added bonus task 3.


def guess_random_number(tries, start, stop):
    random_num = random.randint(start, stop)
    used_nums = []
    while tries != 0:
        user_guess_input = input('Guess a number between 1 and 10: ')

        if not user_guess_input.isdigit():
            print('Please enter a numerical amount. You have lost a try. Guess again.')
            tries -= 1
            print('You have', tries, 'tries remaining.')

        else:
            user_guess = int(user_guess_input)

            if user_guess in used_nums:
                print(
                    'You have already guessed this number. You lost a try. Guess again.')
                tries -= 1
                print('You have', tries, 'tries remaining.')

            elif user_guess < start or user_guess > stop:
                print('Invalid number. You lost a try. Guess within range:',
                      start, '-', stop)
                tries -= 1
                print('You have', tries, 'tries remaining.')

            elif user_guess > random_num:
                print('Too high. Guess again')
                tries -= 1
                print('You have', tries, 'tries remaining.')

            elif user_guess < random_num:
                print('Too low. Guess again.')
                tries -= 1
                print('You have', tries, 'tries remaining.')

            elif user_guess == random_num:
                print('You guessed right!')
                return

            used_nums.append(user_guess)

    if tries == 0:
        print('You have run out of tries. You lose')
        print('The number was', random_num)

# Task 2


def guess_random_num_linear(tries, start, stop):
    tries = 5
    random_num = random.randint(start, stop)
    print('The number the computer is looking for is: ', random_num)
    for x in range(start, stop+1):
        if x == random_num:
            print('The number has been found.', random_num)
            return
        else:
            print('The program is guessing....')
            print('The number has not been found.')
            tries -= 1
            print('Number of tries left: ', tries)

        if tries == 0:
            print('The computer has run out of tries.')
            return


# Task 3
def guess_random_num_binary(tries, start, stop):
    lower_bound = start
    upper_bound = stop - 1
    target_num = random.randint(start, stop)
    print('The number the computer is looking for is', target_num)

    while lower_bound <= upper_bound:
        tries -= 1
        pivot = (lower_bound + upper_bound)//2
        if pivot == target_num:
            print('The number has been found.', target_num)
            return pivot

        if pivot < target_num:
            lower_bound = pivot + 1
            print('The computer guessed:', pivot)
            print('Guessing higher...')

        else:
            upper_bound = pivot - 1
            print('The computer guessed:', pivot)
            print('Guessing lower...')

        if tries == 0:
            print('The computer has no more guesses remaining.')
            print('The number has not been found.')
            return


# Bonus task 2
def input_function():
    # added contingencies for incorrect input
    while True:
        tries = input('How many tries would you like?: ')
        if not tries.isdigit():
            print('Please enter a positive number.')
        elif tries == '0':
            print('Please enter a number greater than 0.')
        else:
            tries = int(tries)
            break
    while True:
        start = input('What would you like your lowest number to be?: ')
        if not start.isdigit():
            print('Please enter a positive number.')
        elif start == '0':
            print('Please enter a number greater than 0.')
        else:
            start = int(start)
            break
    while True:
        stop = input('What would you like your highest number to be?: ')
        if not stop.isdigit():
            print('Please enter a positive number.')
        elif int(stop) < start:
            print('Please enter a number higher than your starting number.')
        else:
            stop = int(stop)
            break

    option = input('Choose 1 for linear search or 2 for binary search: ')
    if option != '1' and option != '2':
        print('Please choose 1 or 2')
        input_function()
    elif option == '1':
        guess_random_num_linear(tries, start, stop)
    elif option == '2':
        guess_random_num_binary(tries, start, stop)


# guess_random_number(5, 1, 10)
# guess_random_num_linear(5, 1, 10)
# guess_random_num_binary(4, 1,100)
input_function()
