import random

def play():
    
    presentation()
    secret_word = load_secret_word()
    right_letters = initialize_right_letters(secret_word)

    hanged = False
    right = False
    errors = 7

    print(right_letters)
    while (not hanged and not right):
        
        guess = ask_guess()

        if (guess in secret_word):
            mark_right_guess(guess, right_letters, secret_word)
            
        else:
            errors -= 1
            draw_hangman(errors)
            print(f"That letter don't exist in this word. You have left {errors} tries.")

        hanged = errors == 0
        right = "_" not in right_letters
        print(right_letters)

    if (right):
        show_winning_message()
    else:
        show_losing_message(secret_word)
    
    play_again_message()

def presentation():
    print("****************************")
    print("Welcome to the hangman game!")
    print("****************************")

def load_secret_word():
    archive = open(r"C:\Users\jhogo\OneDrive\Documentos\Estudos\Alura\python\words.txt", "r")#Here, use your diretory
    words = []

    for line in archive:
        line = line.strip()
        words.append(line)

    archive.close()

    number = random.randrange(0,len(words))
    secret_word = words[number].upper()
    return secret_word

def initialize_right_letters(word):
    return ["_" for letter in word]

def ask_guess():
    guess = input("Wich letter? ")
    guess = guess.strip().upper()
    return guess

def mark_right_guess(guess, right_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            right_letters[index] = letter
        index += 1

def show_winning_message():
    print("Congratulations! You guessed the right word!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def show_losing_message(secret_word):
    print(f"You lost. The secret word was {secret_word}.")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def play_again_message():
    print("Do you want to play again?")
    print("(1) Yes (2) No ")
    answer = int(input(""))

    if (answer == 1):
        play()
    else:
        print('Game over')

def draw_hangman(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    play()