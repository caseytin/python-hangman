from gameClass import *
from characterClass import * 
HANGMAN = "hangman"
def main():
    word = input("What is the hangman word?: ")
    game = Game(word)
    while game.validateWord() == True:
        game = Game(word)
        print(game)
        print(game.getWord())
        char = True
        while char == True:
            character = input("What is your character?: ")
            game.setChar(Character(character))
            print(game.getCharacter())
            print(game.getInvalidCharacterOutput())
            print(game.isInWord())
            game.appendToCharLists()
            print(game.getInvalidCharacterOutput())
            print(game.getInvalidInputCounter())
            print(game.getValidLetters())
            game.appendToValidLettersWord()
            print(game.getDisplayResults())
            game.lenOfWord()
            print(game.hasWon())
            char = True
        word = input("What is the hangman word?: ")
main()
