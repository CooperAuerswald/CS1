import random                                                                                           #adds random index
import time                                                                                             #adds time index                                                                                        
answers = ["Yes!", "No", "Probably", "Probably Not", "Only If You Try Harder","Go Ask Your Dad"]        #list of possible answers

while True:                                                                                             #forever loop
    question = input ("???")                                                                            #prompts user     
    print ("thinking...")                                                                               #displays "Thinking..."
    time.sleep(3)                                                                                       #pauses code for 3 seconds
    print (random.choice(answers))                                                                      #prints random word from the list
    time.sleep(2)                                                                                       #pauses code for 2 seconds before restarting
            
