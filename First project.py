<<<<<<< HEAD
import random
number = random.randint(1, 10)
number_of_guesses = 0
player_name = input("Hello, What's your name?")
print('okay! '+ player_name+ ' I am guessing a number between 1 and 10')
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses +=1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
    if guess == number:
        break
    if guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries! ')

    else:
        print ('You did not guess the number, The number was ' + str(number))

=======
import random
number = random.randint(1, 10)
number_of_guesses = 0
player_name = input("Hello, What's your name?")
print('okay! '+ player_name+ ' I am guessing a number between 1 and 10')
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses +=1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
    if guess == number:
        break
    if guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries! ')

    else:
        print ('You did not guess the number, The number was ' + str(number))

>>>>>>> d8d9cc54ae37be56c5feab553cb66962fdf3e1f8
