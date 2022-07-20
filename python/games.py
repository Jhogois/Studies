import hangman
import guessing

def choose_game():
    print("*****************************")
    print("******Choose your game!******")
    print("*****************************")

    print("(1) Hangman game (2) guessing game")

    game = int(input("Wich game do you wanna play? "))

    if (game == 1):
        print("Initiating the Hangman Game!")
        hangman.play()
    elif (game == 2):
        print("Initiating the Guessing Game!")
        guessing.play()

if (__name__ == "__main__"):
    choose_game()