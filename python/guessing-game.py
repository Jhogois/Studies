print("****************************")
print("Welcome to my guessing-game!")
print("****************************")

secret_number = 42

guess_str = input("type your number: ")

print("You typed", guess_str)

guess = int(guess_str)

if (secret_number == guess):
    print("You guessed right")
else:
    print("You guessed wrong") 

print('Game over')