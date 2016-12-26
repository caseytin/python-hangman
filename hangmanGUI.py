'''
Benjamin Pearlstone, Casey Tin
bpearls1@binghamton.edu, ctin1@binghamton.edu
Sections B57 and B54, CAs: Margie and Julie
Final Project - Hangman GUI
'''

#-- Imports ------------------------------------------------------------------
import os
from tkinter import *
from tkinter import messagebox
from gameClass import *
from characterClass import *

#-- Class FirstPage ----------------------------------------------------------
# Welcome/Start page for the Hangman game. In order to start the game, a
# valid word must be inputted.

class FirstPageGUI:

  #-- Constructor ------------------------------------------------------------
  
    # -------------------------------- CASEY'S CODE --------------------------
  # Params: windows - the Tkinter root window
  def __init__(self, windows):
    # Creates an instance of game
    self.word = Game(None)
    # Sets initial window to root window
    self.tkOne = windows
    # Coordinates of the window
    self.tkOne.geometry('400x300')
    # Title of window
    self.tkOne.title('Welcome to Hangman!')

    # Frames 
    self.tkOneFrame = Frame(self.tkOne)
    self.tkOneFrame.grid(row = 0,
                         column = 0,
                         sticky = W+E+N+S)
    # Make the frames resizable
    Grid.rowconfigure(windows, 0, weight = 1)
    Grid.columnconfigure(windows, 0, weight = 1)
    
    # Widgets
    # 
    self.__titleImg = PhotoImage(file = 'imagetitle.gif')
    self.__titleImgLabel = Label(self.tkOne,
                                 image = self.__titleImg)
    self.__titleImgLabel.grid(row = 0,
                              column = 5,
                              sticky = W+E+N+S)
    self.__welcomeLabel = Label(self.tkOne,
                                text = 'WELCOME TO HANGMAN!',
                                fg = "dark blue",
                                font = ("Courier", 24, "bold"))
    self.__welcomeLabel.grid(row = 9,
                             column = 5,
                             padx = 10,
                             pady = 10 )                              

    self.__titleLabel = Label(self.tkOne,
                              text = 'Enter a word to start the game: ',
                              fg = "blue",
                              font = ("Courier", 16))                        
    self.__titleLabel.grid(row = 10,
                           column = 5,
                           sticky = W+E+N+S)
    
    self.__titleEntry = Entry(self.tkOne,
                              w = 20)
    self.__titleEntry.bind('<Return>', self.unlockButton)
    self.__titleEntry.grid(row = 11,
                           column = 5,
                           sticky = W+E+N+S)

    self.__startButton = Button(self.tkOne,
                                text = 'Start Game',
                                font = ("Courier", 14),
                                state = DISABLED,
                                command = self.goToSecondPage)
                          
    self.__startButton.grid(row = 12,
                            column = 5,
                            sticky = W+E+N+S)
  #-- Event handlers----------------------------------------------------------
    # -------------------------------- BEN'S CODE ----------------------------

  # unlockButton: Enables button if the entered word is valid
  # Param: self, event
  
  def unlockButton(self, event):
    self.word = Game(self.__titleEntry.get())
    self.__titleEntry.delete(0,END)
    if self.word.validateWord():
      self.__startButton.config(state = ACTIVE)
    elif self.__titleEntry.get() == "":
      self.__startButton.config(state = DISABLED)
  # goToSecondPage: Opens game window for Hangman
  # Param: self
  def goToSecondPage(self):
    windowTwo = Toplevel(self.tkOne)
    name = SecondPageGUI(windowTwo, self.word)
    self.__startButton.config(state = DISABLED)
    
#-- Class SecondPageGUI ------------------------------------------------------
# Game page for the Hangman Game. Appears after the user has entered a word
# at the Start page, and stimulates the classic Hangman guessing game. Whether
# the player(s) win or lose, they have the option of quitting the game or
# restarting the game for a new round of Hangman.

class SecondPageGUI:
  
  #-- Constants ------------------------------------------------------------

  ONE_ERROR = 1
  TWO_ERRORS = 2
  THREE_ERRORS = 3
  FOUR_ERRORS = 4
  FIVE_ERRORS = 5
  SIX_ERRORS = 6
  ERROR_LIMIT = 7

  GALLOW = 'gallow.gif'
  HEAD = 'head.gif'
  BODY = 'body.gif'
  LEFT_ARM = 'leftarm.gif'
  RIGHT_ARM = 'rightarm.gif'
  LEFT_LEG = 'leftleg.gif'
  RIGHT_LEG = 'rightleg.gif'
  DEAD = 'deadface.gif'

  INVALID_CHAR_MSG = 'Input must be one letter, in the alphabet.'
  VALID_CHAR_MSG = ''

  #-- Constructor ------------------------------------------------------------
    # -------------------------------- CASEY'S CODE --------------------------
  def __init__(self, windows, word):
    # Creates 
    self.word = word
    # Sets second window to root window
    self.tkTwo = windows
    # Title of second window(Game window)
    self.tkTwo.title('Playing: Hangman')
    self.tkTwo.geometry('450x500')

    # Widgets 
    self.gameImg = PhotoImage(file = 'gallow.gif')
    self.gameLabel = Label(self.tkTwo,
                             image = self.gameImg)
    self.gameLabel.image = self.gameImg
    self.gameLabel.grid(row = 0, column = 10)
                                                                   

    self.__charEntryBox = Entry(self.tkTwo,
                                w = 50)
    self.__charEntryBox.bind('<Return>', self.charEntry)
    self.__charEntryBox.grid(row = 5,
                             column = 10,
                             pady = 10)

    self.__validCharLabel = Label(self.tkTwo,
                                  text = "",
                                  font = ("Courier", 13))
    self.__validCharLabel.grid(row = 6,
                               column = 10,
                               sticky = W+E+N+S)

    self.__currentWordState = Label(self.tkTwo,
                                    text = self.firstValue(),
                                    font = ("Courier", 20),
                                    fg = "magenta")
    self.__currentWordState.grid(row = 4,
                                 column = 10,
                                 sticky = W+E+N+S,
                                 padx = 10,
                                 pady = 10)
    self.__invalidCharBox = Label(self.tkTwo,
                                  text = 'Invalid characters',
                                  width = 20,
                                  font = ("Courier", 14),
                                  fg = "red",
                                  borderwidth = 2)
    self.__invalidCharBox.grid(row = 7,
                               column = 10,
                               sticky = W+E+N+S)
    self.__invalidCharLabel = Label(self.tkTwo,
                                    text = "",
                                    width = 20,
                                    font = ("Courier", 13),
                                    fg = "red")
    self.__invalidCharLabel.grid(row = 8,
                                 column = 10,
                                 sticky = W+E+N+S)
  #-- Event handlers ---------------------------------------------------------
    # -------------------------------- BEN'S CODE ----------------------------

  # Provides the number of letters in the initial user's inputted word, for
  # the other player 
  def firstValue(self):
    self.word.lenOfWord()
#    print(self.word.getFirstSeenValue()) ##debug
    return self.word.getFirstSeenValue()
  
  # Performs multiple methods when other player(s) input(s)
  # a character to guess
  # Param: self, event
  def charEntry(self, event):
    # Gets the inputted character from the entry box
    inputtedChar = self.__charEntryBox.get()
    # Resets the entry box when <Enter> has been hit
    self.__charEntryBox.delete(0, END)
    #print(inputtedChar) ##debug
    self.word.setChar(Character(inputtedChar))
    #print(self.word.getCharacter()) ##debug
    # If the word is not one character long
    if self.word.isOneChar() == False:
      # Display the invalid character message
      self.__validCharLabel.config(text = self.INVALID_CHAR_MSG)
    # If the word is one character long
    elif self.word.isOneChar():
      # Display the valid character message (empty string)
      self.__validCharLabel.config(text = self.VALID_CHAR_MSG)
      # Append the character to the instance 
      self.word.appendToCharLists()
      # Append the character to the list of valid characters
      self.word.appendToValidLettersWord()
      self.__currentWordState.config(text = self.word.getDisplayResults())
#      print(self.word.getWinningWord()) ##debug
#      print(self.word.hasWon()) ##debug
      # If the word passes the check from the hasWon() predicate function
      if self.word.hasWon():
        # Display a message box, titled 'Congratulations!'
        self.youWon = messagebox.askyesno('Congratulations!',\
        "Hooray, you've won Hangman!\n Would you like to play again?")
        # If the player wants to play again (clicks 'Yes' button)
        if self.youWon == True:
          # Reset all of the instances
          self.word.resetAll()
          # Destroy the second window, leaving only the first window open
          self.tkTwo.destroy()
        # If the player does not want to play again (clicks 'No' button)
        elif self.youWon == False:
          # Exits the entire program
          os._exit(0)
          
    # If the word passes the check from the hasLost predicate function
      elif self.word.hasLost():
        # Updates the final image that corresponds with the error limit
        updatedImage = PhotoImage(file = self.DEAD)
        self.gameLabel.config(image = updatedImage)
        self.gameLabel.image = updatedImage
        # Adds the last invalid character to the label of invalid characters
        self.__invalidCharLabel.config(\
          text=self.word.getInvalidCharacterOutput())
        # Display a message box, titled 'Oh no!'
        self.youLost = messagebox.askyesno('Oh no!',\
                                            'Sorry, you lose!\n' + \
                                           'Would you like to play again?')
        # If the player wants to play again (clicks 'Yes' button)
        if self.youLost == True:
          # Reset all of the instances
          self.word.resetAll()
          # Destroy the second window, leaving only the first window open
          self.tkTwo.destroy()
        # If the player does not want to play again (clicks 'No' button)
        elif self.youLost == False:
          # Exits the entire program
          os._exit(0)     
    # Sets error count equal to the function that counts the number of
    # invalid character inputs
    errorCount = self.word.getInvalidInputCounter()
    # Calls the function that updates the hangman image on the second window
    self.updateErrorImage(self.gameLabel, errorCount)
    
  # updateErrorImage: Updates the hangman image depending on the
  # number of errors(invalid character inputs) made by the player
  # Param: self, gameLabel, errorCount
  def updateErrorImage(self, gameLabel, errorCount):
    # If there is one error
    if errorCount == self.ONE_ERROR:
      # Updates the image that corresponds with one error
      updatedImage = PhotoImage(file = self.HEAD)
      gameLabel.config(image = updatedImage)
      gameLabel.image = updatedImage
      # Sets the text in the invalid character label
      self.__invalidCharLabel.config(text =\
                                     self.word.getInvalidCharacterOutput())
    # If there are two errors
    elif errorCount == self.TWO_ERRORS:
      # Updates the image that corresponds with two errors
      updatedImage = PhotoImage(file = self.BODY)
      gameLabel.config(image = updatedImage)
      gameLabel.image = updatedImage
      # Sets the text in the invalid character label
      self.__invalidCharLabel.config(text =\
                                     self.word.getInvalidCharacterOutput())
    # If there are three errors
    elif errorCount == self.THREE_ERRORS:
      # Updates the image that corresponds with three errors
      updatedImage = PhotoImage(file = self.LEFT_ARM)
      gameLabel.config(image = updatedImage)
      gameLabel.image = updatedImage
      # Sets the text in the invalid character label
      self.__invalidCharLabel.config(text =\
                                     self.word.getInvalidCharacterOutput())
    # If there are four errors
    elif errorCount == self.FOUR_ERRORS:
      # Updates the image that corresponds with four errors
      updatedImage = PhotoImage(file = self.RIGHT_ARM)
      gameLabel.config(image = updatedImage)
      gameLabel.image = updatedImage
      # Sets the text in the invalid character label
      self.__invalidCharLabel.config(text =\
                                     self.word.getInvalidCharacterOutput())
    # If there are five errors
    elif errorCount == self.FIVE_ERRORS:
      # Updates the image that corresponds with five errors
      updatedImage = PhotoImage(file = self.LEFT_LEG)
      gameLabel.config(image = updatedImage)
      gameLabel.image = updatedImage
      # Sets the text in the invalid character label
      self.__invalidCharLabel.config(text =\
                                     self.word.getInvalidCharacterOutput())
    # If there are six errors
    elif errorCount == self.SIX_ERRORS:
      # Updates the image that corresponds with six error
      updatedImage = PhotoImage(file = self.RIGHT_LEG)
      gameLabel.config(image = updatedImage)
      gameLabel.image = updatedImage
      # Sets the text in the invalid character label
      self.__invalidCharLabel.config(text =\
                                     self.word.getInvalidCharacterOutput())
    

#-- Main function ------------------------------------------------------------
# Creates the window, an instance of the start page, and initiates
# the tkinter loop

def main():

  #Creates a Tkinter root window
  windows = Tk()
  #Creates an instance of the first page (the Welcome screen)
  FirstPageGUI(windows)
  windows.mainloop()
  
main()
