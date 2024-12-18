                                                    #cat
import random                                       #Imports random index
import time                                         #Imports time index
user_score = 0                                      #Creates score variable
options = ["Rock", "Paper", "Scissors"]             #List of options for bot to choose
while True:                                         #Forever loop
    bot = random.choice (options)                   #Bot picks a random option from the list
    user = input ("Rock, Paper, or Scissors?")      #Prompts the user for Rock Paper or Scissors
    print (bot)                                     #Shows the bot's answer
    if bot == user:                                 #If the bot's answer is the same as the user's:
        print("TIE")                                #Displays "TIE"
    elif bot== "Rock" and user== "Scissors":        #If the bot is rock and player is scissors:
        print("You Lose")                           #Print "You Lose"
        user_score -=1                              #Subtracts one from user score
        print (user_score)                          #Displays user score
    elif bot== "Paper" and user== "Rock":           #If the bot is Paper and user is Rock:
        print ("You Lose")                          #Print "You Lose"
        user_score -=1                              #Subtracts one from user score
        print (user_score)                          #Displays user score
    elif bot== "Scissors" and user== "Paper":       #If the bot is scissors and user is paper:
        print ("You Lose")                          #Print "You Lose"
        user_score -=1                              #Subtracts one from user score
        print (user_score)                          #Displays user score
    elif user== "Rock" and bot== "Scissors":        #If the user is Rock and bot is Scissors:
        print ("YOU WIN!")                          #Print "YOU WIN!"
        user_score +=1                              #Adds one point for the win
        print (user_score)                          #Displays score
    elif user== "Paper" and bot== "Rock":           #If the user is paper and bot is rock:
        print ("YOU WIN!")                          #Print "YOU WIN!"
        user_score +=1                              #Adds one to the score
        print (user_score)                          #Displays current score
    elif user== "Scissors" and bot== "Paper":       #If user is Scissors and bot is Paper:
        print ("YOU WIN!")                          #Print "YOU WIN!"
        user_score +=1                              #Adds one to the score
        print (user_score)                          #Displays current score
    else: print ("Try Again")                       #Otherwise print "Try Again"
