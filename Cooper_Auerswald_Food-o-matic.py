import random
foods = ["Cauliflower", "Tilapia Fillet", "Pork Loin", "Salmon", "Potatoes", "3 Color Squash", "Eggplant", "Steak", "Baguette"]                                             #List of possible entres
prices = [20,25,28,30,18,20,22,30,20]                                                                                                                                       #list of corresponding prices
flairs = ["with balsamico", "With Garlic & Olive Oil", "With Minted Yogurt", "With Chutney", "Salad", "With Salsa", "Over sticky rice", "Au Jus", "With Basmati Rice"]      #list of possible flairs

num_of_items = int(input("How many items?"))                                                                                                                                #asks user for a number of items

for i in range(num_of_items):                                                                                                               
    food = random.choice(foods)                                                                                                                                             #picks a random food
    flair = random.choice(flairs)                                                                                                                                           #picks a random flair
    index = foods.index(food)                                                                                                                                               #finds index from entree
    price = prices[index]                                                                                                                                                   #finds the matching index for price
    print(f'{food} {flair}, ${price}')                                                                                                                                      #prints the food with the flair and price
