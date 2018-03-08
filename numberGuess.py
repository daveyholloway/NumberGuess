# This is a boolean that we set to True when we've guessed the number
solved = False

# This variable is used to store the number of guesses
numberOfGuesses = 0

# This is the low end of the range we're guessing in
lowerNumber = 1

# This is the high end of the range we're guessing in
higherNumber = 100

# Ask the user to think of a number in the range between low and high
print("Think of a number between " + str(lowerNumber) + " and " + str(higherNumber) + ".")

# Keep doing this while we've not solved the guess
while (solved == False):

    # Guess half way between the low and high number, used the int function to avoid
    # any halves!
    computerGuess = lowerNumber + int((higherNumber - lowerNumber)/2)

    # Add 1 to the guess counter
    numberOfGuesses = numberOfGuesses + 1

    # Print the guess and check to see if it's correct
    print("I'm guessing that your number is " + str(computerGuess) + "\n")
    userAnswer = input("Am I right (Y), too low (L) or too high (H) ?\n")

    if userAnswer.upper() == "Y" :
       # The user says we've guessed it so set solved to True and finish
       print("Your number was " + str(computerGuess) + " how clever am I?")
       solved = True
   
    elif userAnswer.upper() == "L" :
       print("I guessed too low...\n")
       # So number needs to be between the guess and the high number so leave the high number
       # as it is and change the low number to be the last guess plus 1...
       lowerNumber = computerGuess + 1 

    elif userAnswer.upper() == "H" :
       print("I guessed too high...\n")
       # So number needs to be between the low number and the guess so leave the low number
       # as it is and change the high number to be the guess minus 1 ...
       higherNumber = computerGuess - 1

    else:
        print("Please type 'Y', 'L' or 'H'\n")
        # The user didn't enter an answer we recognise

# Tell the user we're finished and show the number of turns   
print ("Finished after " + str(numberOfGuesses) + " guesses!\n")
