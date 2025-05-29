'''
Author: Cooper Auerswald
Sources: Ms. Marciano, CS1 Google Classroom
Description: Allows user to keep account passwords
Date: 5/23/2025
Challenges:  Require Password to Enter, Change Entry
Bugs: N/A
'''

def add_entry (websites, usernames, passwords):
    '''
        adds item to parallel array lists
    Args:
    websites (list): list of websites
    usernames (list): List of usernames
    passwords (List): list of passwords
    Returns:
        parallel array: New parallel array entries in each list'''
    
    website = input ("input website")
    username = input ("input username")
    password = input ("input password")
    websites.append (website)
    usernames.append (username)
    passwords.append (password)


def print_entry (website, username, password):
    print (f"{website}, {username}, {password}")
def get_index (websites):
    while True:
        website = input ("What website?")
        if website in websites:
            websites.index (website)
            return 
        else:
            print ("404 Website Not Found")
#def print_entry(website, username, password):
    #print in a f string
#def get_index(websites):
    #forever loop
        #ask for a website
        #if website is in websites:
            #return the index of website in websites
        #else:
            #print not here

def main ():
    websites=[]
    usernames=[]
    passwords=[]

    while True:
        selection = input ('''What would you like to do? Enter "q" to quit
1. New entry  
2. See all entries  
3. Access a specific entry
                        ''').lower()
        
        if selection == "q":
            break
        elif selection == ("1"):
            add_entry(websites, usernames, passwords)
        elif selection == ("2"):
            for index in range(len(websites)):
                print_entry(websites[index], usernames[index], passwords[index])
        elif selection == ("3"):
            index = get_index(websites)                         
            print_entry(websites[index], usernames[index], passwords[index])

main_pwd = input ("Create Main Password")
pwd_ask = input ("what is your Main Password")
if pwd_ask == main_pwd:
     print ("Welcome")
     main ()
else: print ("Try Again")
    
 
