'''
Author: Cooper Auerswald
Date: 5/29/2025
Description: Practicing functions for CS1 Class
Bugs: N/A
Challenges: Get_Initials
Sources: Ms. Marciano, Google Classroom
'''

import random                                           
def chorus():                                           
    '''
    Prints the chorus of a song
    Args:
        None
    Returns:
        print: chorus
    '''
    print('''                                           
I got a fear, dear, that it's gonna end
Won't you get angry at me, say you love me again
I got a fear dear, that it's a Friday spark
You only love me like you mean it when it's after dark
   ''')
def sing_song ():                                       
    '''
    Use the chorus function to sing the entire song
    Args:
        None
    Returns:
        print: Entire song
    '''
    print ('''    
Pluck strings on porches, a poor boys' choir
And my blood's at a boil, there ain't no fire
I just love the way the light beams in
But I got bad news, I'm fearin' Friday again
           
Chokin' on some bourbon when you roll up
Said, "Boy, you gotta face it, you's ain't that tough"
There's a house hoppin' on the edge of town
I'm revved up, thirsty, and ready to drown
    ''')
    chorus ()                                           
    print ('''
    We can hide out tonight out where the trees gеt clear
Those pleasе-you-eyes are a man's worst fear
There's a name saved on your heart's gravestone
Saturday's coming, I fear I'm waking alone
    ''')
    chorus ()                                                                 
    chorus ()  

def add (x, y):                                         
    '''
    Adds two numbers
    Args:
        x (int) : first number
        y (int) : second number
    Returns: 
        print: sum of both numbers
    '''
    print (x+y)                                         

def print_list (list_1):                                
    for i in list_1:                                    
        print(i)                                        
def in_list(list_1, element):                           
    return element in list_1                            
def is_integer(number):                                 
    '''
    Prints a list one item at a time
    Args:
        list_1 (list) a list
    Returns: 
        print: list
    ''' 
    try:                                                
        number = int(number)                            
        return True                                     
    except:                                             
        return False  
                                     

def get_integers ():                                    
    '''
    Gets the integers from the 2 numbers
    Args:
        number1 (str) a number
        number2 (str) another number
    Returns: 
        return the numbers as integers 
    '''                                                          
    while True:                                        
        number1 = input ("Input the first number")      
        number2 = input ("Input the second number")     
        
        if is_integer (number1) and is_integer(number2):                                  
            return int(number1), int(number2)   

def get_random ():   
    '''
    prints a random number between those of get_integers
    Args:
        none
    Returns: 
        print: random integer between the two
    '''                                     
    a,b = get_integers ()                               
    print(random.randint(a,b))  
                                                            

def count_vowels ():
    '''
    Counts vowels in a string
    Args:
        vowels (int)
    Returns: 
        print: vowels
    '''                                      
    word = input("Insert word: ")                        
    vowels = 0          

    for c in word:                                      
        if c in ['a', 'e', 'i', 'o', 'u']:                                     
            vowels += 1                                     
    return vowels                                     
                                   

def get_initials (fullname):
    '''
    Prints initials of a full name
    Args:
       fullname (str) a full name
    Returns: 
        print: Initials
    '''                                  
    names = fullname.split(' ')
    initials = ""
    for name in names:
        initials += name [0]
    return initials
def main ():
    while True:
        selection=input('''
What would you like to do? (q to quit)
    1. sing song
    2. add
    3. print list
    4. in list
    5. is integer
    6. get integers
    7. get random
    8. count vowels
    9. get initials 
    ''')  
        if selection == ("q"):
            break  
        elif selection == ("1"):
            sing_song ()
        elif selection == ("2"):
            add (6,7)
        elif selection == ("3"):
            foods = ["Burger", "Fries", "Milkshake"]
            print_list (foods)
        elif selection == ("4"):
            print(in_list(foods, 'hello'))  
        elif selection == ("5"):
            is_integer ()
        elif selection == ("6"):
            get_integers ()
        elif selection == ("7"):
            get_random ()
        elif selection == ("8"):
            print(count_vowels ()) 
        elif selection == ("9"):
            print(get_initials ("Cooper Auerswald") )
        else:
            print ("try again")

main ()
