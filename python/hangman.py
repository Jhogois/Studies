def play():
    print("****************************")
    print("Welcome to the hangman game!")
    print("****************************")

    archive = open("words.txt", "r")
    words = []

    for line in archive:
        line = line.strip()
        words.append(line)

    archive.close()

    print(words)

    secret_word = "banana".upper()
    right_letters = ["_" for letter in secret_word]

    hanged = False
    right = False
    errors = 6

    print(right_letters)
    while (not hanged and not right):
        guess = input("Wich letter? ")
        guess = guess.strip().upper()

        if (guess in secret_word):
            index = 0
            for letter in secret_word:
                if (guess == letter):
                    right_letters[index] = letter
                index += 1
            
        else:
            errors -= 1
            print(f"That letter don't exist in this word. You have left {errors} tries.")

        hanged = errors == 0
        right = "_" not in right_letters
        print(right_letters)

    if (right):
        print("Congratulations! You guessed the right word!")
    else:
        print(f"You lost. The secret word was {secret_word}.")
    
    print("Do you want to play again?")
    print("(1) Yes (2) No ")
    answer = int(input(""))

    if (answer == 1):
        play()
    else:
        print('Game over')

if (__name__ == "__main__"):
    play()