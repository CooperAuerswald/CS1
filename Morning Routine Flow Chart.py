import time
import datetime
print ("ALARM")                                             #displays "ALARM"
current_time = datetime.datetime(2024, 10, 25, 6, 30, 0)    #sets time to 6:30
print (current_time.strftime("%H:%M:%S"), end='\r')         #displays time
while True:                                                 #forever loop
    get_up = input("\nget up? y/n:")                        #asks if user wants to get up

    if get_up == "n":                                       #if you get up
        print ("Sleep for a few more minutes")              #displays "Sleep for a few more minutes"
        time.sleep (2)                                      #pauses code for 2 seconds
        print ("Mom Wakes Me Up")                           #Displays "Mom wakes me up"
        current_time += datetime.timedelta(minutes=5)       #adds 5 minutes to time
        print(current_time.strftime("%H:%M:%S"), end='\r')  #Displays time
        break                                               #ends forever loop
    elif get_up == "y":                                     #yes to getting up
        break                                               #ends forever loop
    else:                                                   #otherwise
        print("Invalid Response")                           #display "Invalid Response"
time.sleep (1)                                              #pause code for 1 second
print(" Shower")                                            #Display "Shower"
time.sleep (1)                                              #pause code for 1 second
print("Dry Off")                                            #display "Dry Off"
current_time += datetime.timedelta(minutes=10)              #adds 10 minutes to time
print(current_time.strftime("%H:%M:%S"), end='\r')          #Displays time
time.sleep (1)                                              #pauses code for 1 second
print (" Is it cold?")                                      #Display "Is it cold?"
time.sleep (1)                                              #pauses code for 1 second

while True:                                                 #forever loop
    cold = input ("Cold? y/n:")                             #asks if its cold

    if cold == "y":                                         #if it is cold:
        print ("Put on a quarter zip")                      #Displays "Put on a quarter zip"
        break                                               #ends forever loop
    elif cold == "n":                                       #if its not cold:
        print ("Put on a polo shirt")                       #display "Put o a polo shirt"
        break                                               #end forever loop
    else:                                                   #otherwise:
        print ("Invalid Response")                          #display "Invalid Response"
time.sleep (1)                                              #pauses code for 1 second
print ("Brush Teeth")                                       #display "Brush teeth"
time.sleep (1)                                              #pause code for 1 second
print ("Pack Bag")                                          #display "Pack Bag"
time.sleep (1)                                              #pauses code for 1 second
print ("Go to School")                                      #Display "Go to School"
current_time += datetime.timedelta(minutes=45)              #Add 45 minutes to time
print(current_time.strftime("%H:%M:%S"), end='\r')          #Displays time

        
