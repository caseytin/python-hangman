'''
Benjamin Pearlstone, Casey Tin
bpearls1@binghamton.edu, ctin1@binghamton.edu
Sections B57 and B54, CAs: Margie and Julie
Final Project - Hangman LOGIC CLASS (Game)
'''

#-- Imports ------------------------------------------------------------------

# For sound playback
import subprocess

# For character input
import characterClass

#-- Class Game ---------------------------------------------------------------

# Application logic game class that runs the Hangman game
# No params
class Game:
    
    #-- Constants ------------------------------------------------------------
    # Sound file str
    CORRECT_MP3 = "correct.mp3"
    # Limit of incorrect imputs
    ERROR_LIMIT = 7

    
# -- Constructor -------------------------------------------------------------

    # -------------------------------- CASEY'S CODE --------------------------

    # Params: Word - (instance of Game class input)
    def __init__(self, word):
       
        # Initial player's word to be guessed 
        self.__word = word
        # Empty string to be replaced by Character class input
        self.__charInput = ""
        # Invalid characters string for user
        self.__invalidCharacterOutput = ""
        # List of vali letters for predicate functios
        self.__validLetters = ""
        # Results to be displayed for user
        self.__displayResults = ""
        # Other player(s)' guessed word
        self.__winningWord = ""
        # Counter; must reset
        self.__invalidInputCounter = 0
        # For the first value presented; must reset
        self.__firstSeenValue = ""
       
# -- Accessors ---------------------------------------------------------------

    # ------------------------------- CASEY'S CODE ---------------------------
    
    # getWord: Gets word used at beginning of game
    # Param: self
    # Return: Word input to Game Class
    def getWord(self):
        return self.__word
    
    # getWinningWord: Gets her player(s)' guessed word
    # Param: self
    # Return: Version of inputted word for user.
    def getWinningWord(self):
        return self.__winningWord

    # getCharacter: Gets character that other player(s) input(s)
    # Param: self
    # Return: The inputter character from the Character class
    def getCharacter(self):
        return self.__charInput
    
    # getInvalidCharacterOutput: Gets list of letters that were not in the word
    # Param: self
    # Return: The invalid characters in word sepesrated by spaces
    def getInvalidCharacterOutput(self):
        return self.__invalidCharacterOutput

    # getValidLetters: Gets list of letters that are in the word
    # Param: self
    # Return: The str of letter in the word
    def getValidLetters(self):
        return self.__validLetters
    
    # getDisplayResults: Gets word filled in
    # Param: self
    # Return: Results of how many correct letters the player has
    def getDisplayResults(self):
        return self.__displayResults

    # getInvalidInputCounter: Gets the number of invalid inputs
    # Param: self
    # Return: Counter of invalid inputs
    def getInvalidInputCounter(self):
        return self.__invalidInputCounter
    
    # Gets the initial value of the other player(s)' guessed word
    # Param: self
    # Return: Underscores for how many letters there in the word.
    def getFirstSeenValue(self):
        return self.__firstSeenValue
    
# -- Predicates --------------------------------------------------------------

    # Checks if inputted character is a valid character
    # Param: self
    # Return: bool
    def isOneChar(self):
        return self.__charInput.isalpha() and len(self.__charInput) == 1

    # Checks if inputted character is in the inputted word
    # Param: self
    # Return: bool
    def isInWord(self):
        return self.__charInput.upper() in self.__word \
               or self.__charInput.lower() in self.__word

    # -------------------------- BEN'S CODE:----------------------------------
    
    # Checks if inputted word is valid
    # Param: self
    # Reutrn: bool
    def validateWord(self):
        return self.__word.isalpha()

    # Checks if the character inputted has already been used
    # Param: self
    # Return: bool
    def isCharacterAlreadyUsed(self):
        return self.__charInput.upper() in self.__validLetters\
               or self.__charInput.upper() in self.__invalidCharacterOutput
    
    # Checks if the other player(s)' guessed word matches the initial
    #   player's inputted word
    # Param: self
    # Return:
    def hasWon(self):
        return self.__winningWord.upper() == self.__word.upper()
    
    # Checks if the user has reached the maximum amount of errors
    # Param: self
    # Return: bool
    def hasLost(self):
        return self.__invalidInputCounter == self.ERROR_LIMIT      
    
# Mutators -------------------------------------------------------------------

    # -------------------------------- BEN'S CODE: ---------------------------
    
    # setChar: IMPORTANT, takes from the Character class
    # Param: self
    def setChar(self, character):
        self.__charInput = character.getCharacter()
        
    # appendToCharLists: Filters the incorrect and correct characters
    # Param: self
    def appendToCharLists(self):
        # If the character is not in word
        if self.isInWord() == False:
            if  self.__charInput.upper() not in self.__invalidCharacterOutput:
                self.__invalidCharacterOutput += self.__charInput.upper() + " "
                self.__invalidInputCounter += 1
        # If the character is in the word               
        elif  self.isInWord() == True:
            if self.__charInput.upper() not in self.__validLetters:
                self.__validLetters += self.__charInput.upper()
                
    # appendToValidLettersWord: Updates the other player(s)' entered characters, in a list
    # Param: self
    def appendToValidLettersWord(self):
        self.__displayResults = ""
        self.__winningWord = ""
        subprocess.call(["afplay", self.CORRECT_MP3])
        for self.__char in self.__word.upper():
            if self.__char not in self.__validLetters:
                self.__displayResults += "_ "
            else:
                self.__displayResults += self.__char + " "
                self.__winningWord += self.__char

    # lenOfWord: Provides an underscore for the each character in the length of the word
    # Param: self
    def lenOfWord(self):
        for i in self.__word:
            self.__firstSeenValue += "_ "
            
    # resetAll: Resets all instances needed for the game, so that the user can start
    #   a new game
    # Param: self
    def resetAll(self):
       self.__charInput = ""
       self.__invalidCharacterOutput = ""
       self.__validLetters = ""
       self.__displayResults = ""
       self.__invalidInputCounter = 0
       self.__firstSeenValue = ""
