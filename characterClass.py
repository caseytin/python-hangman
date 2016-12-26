'''
Benjamin Pearlstone, Casey Tin
bpearls1@binghamton.edu, ctin1@binghamton.edu
Sections B57 and B54, CAs: Margie and Julie
Final Project - Hangman LOGIC CLASS (Character)
'''

# BEN'S CODE ----------------------------------------------------------------

#-- Class Character ----------------------------------------------------------
# Application logic character class that provides characters from the
# inputted word
class Character:

# -- Constructor -------------------------------------------------------------
    # PARAMS: character (str) - Input from the user about the character:
    def __init__(self, character):
       self.__character = character
           
# -- Accessors ---------------------------------------------------------------
    # Returns the character 
    def getCharacter(self):
        return self.__character 
