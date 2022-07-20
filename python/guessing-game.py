print("****************************")
print("Welcome to my guessing-game!")
print("****************************")

secret_number = 42
total_attempts = 3

for attempt in range (1, total_attempts + 1):
    print(f"attempt {attempt} of {total_attempts}")
    guess_str = input("type a number between 1 and 100: ")
    print("You typed", guess_str)
    guess = int(guess_str)

    if (guess < 1 or guess > 100):
        print("You must type a number between 1 and 100")
        continue

    right  = guess == secret_number
    bigger = guess > secret_number
    less   = guess < secret_number

    if (right):
        print("You guessed right!")
        break
    else:
        if (bigger):
            print("You guessed wrong! Your guess was bigger than the secret number!") 
        elif (less):
            print("You guessed wrong! Your guess was less than the secret number!")

print('Game over')