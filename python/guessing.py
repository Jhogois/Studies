import random

def play():
    print("*****************************")
    print("Welcome to the guessing game!")
    print("*****************************")

    secret_number = random.randrange(1,101)
    total_attempts = 0
    points = 1000

    print("Wich difficulty level do you prefer?")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Choose your difficulty level: "))

    if (level == 1):
        total_attempts = 20
    elif (level == 2):
        total_attempts = 10
    else:
        total_attempts = 5
    if (level < 1 or level > 3):
        print("The number that you typed is not in the difficulties. Choosing the hard difficulty.")

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
            print("You guessed right and did {} points!".format(points))
            break
        else:
            if (bigger):
                print("You guessed wrong! Your guess was bigger than the secret number!") 
                if (attempt == total_attempts):
                    print("The secret number was {}. You did {} points.".format(secret_number, points))
            elif (less):
                print("You guessed wrong! Your guess was less than the secret number!")
                if (attempt == total_attempts):
                    print("The secret number was {}. You did {} points.".format(secret_number, points))
            lost_points = abs(secret_number - guess) // 3
            points = points - lost_points

    print('Game over')

if (__name__ == "__main__"):
    play()