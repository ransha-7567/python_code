#R.5

''' 09/06/23 Comments
Takes in the user's preferred menu item from either a user generated or default list.

Taking into account the actual time taken to cook said item, this is compared alongside the average cook time.
Depending on how close it gets to the average cook time of the meal, a string is outputted along with the status of
the meal and the tip expected.

These values are developed by using the formula of (average_cook_time - / + standard_deviation). This determines whether
or not the actual cooking time ended up being overcooked / undercooked. And if the value is less than or greater than
a particular calculation, such as (average_cook_time - / + (2 * standard_deviation)). Then a -100% tip can be awarded.




'''

input_food = input() #get food details from user

full_stop = False #false until user inputs "."
options = [] #this will store the food dictionaries

#if user inputs '.' first, put default foods into options 
if input_food == '.':
    full_stop = True
    options = [{'name': 'Budda Bowl (vg)', 'sell_for': 25.0, 'cost_to_make': 20.0, 'cook_time': 10.0, 'cook_time_stdev': 3.0}, 
    {'name': 'Eye Fillet Steak', 'sell_for': 55.0, 'cost_to_make': 25.0, 'cook_time': 7.0, 'cook_time_stdev': 1.0}, 
    {'name': 'Spaghetti Bolognese', 'sell_for': 30.0, 'cost_to_make': 22.0, 'cook_time': 40.0, 'cook_time_stdev': 5.0}, 
    {'name': 'Pad Thai (seafood)', 'sell_for': 22.0, 'cost_to_make': 17.0, 'cook_time': 30.0, 'cook_time_stdev': 1.0}
    ]

#if user inputs foods, save each as a dictionary, and store it in options
input_number = 0
dictionaries = {} #this initializes the food dicionaries
while full_stop == False:  #iterate per user's food input
    if input_food == '.':
        full_stop = True
    else:
        input_list = input_food.split(',')
        dictionaries["food" + str(input_number)] = {
            "name": input_list[0],
            "sell_for": float(input_list[1]), 
            "cost_to_make": float(input_list[2]),
            "cook_time": float(input_list[3]),
            "cook_time_stdev": float(input_list[4])
            }
        options.append(dictionaries["food" + str(input_number)]) #add dictionaries to options
        input_food = input()

        input_number += 1 

#get the menu number for each food in options
menu_number = 0
for i in options:    
    name = i["name"]
    sell_for = float(i["sell_for"])
    cost_to_make = float(i["cost_to_make"])
    cook_time = float(i["cook_time"])
    cook_time_stdev = float(i["cook_time_stdev"])
    menu_number += 1

#get actual cook time and determine tip
if full_stop == True:
    menu_number_input,actual_cook_time = input().split(",") #get menu number and actual cook time, split them into a list

    if int(menu_number_input) <= len(options): #check menu number is valid
        menu_number_input = int(menu_number_input) 
        standard_deviation = options[menu_number_input - 1]["cook_time_stdev"]
        average_cook_time = options[menu_number_input - 1]["cook_time"]
        
        #Define the variables into floats for calculation
        standard_deviation = float(standard_deviation)
        average_cook_time = float(average_cook_time)
        actual_cook_time = float(actual_cook_time)
        food_cooking = options[menu_number_input - 1]["name"]
        
        # Compare actual cook time to mean and standard deviation, print cooking classification + tip required
        if actual_cook_time < (average_cook_time - 2*standard_deviation):
            print(f"{food_cooking} was very undercooked and cooking tip was -100%")
        elif (average_cook_time - 2*standard_deviation) <= actual_cook_time and actual_cook_time <= (average_cook_time - standard_deviation):
            print(f"{food_cooking} was slightly undercooked and cooking tip was 0%")
        elif (average_cook_time - standard_deviation) < actual_cook_time and actual_cook_time < (average_cook_time + standard_deviation):
            print(f"{food_cooking} was well cooked and cooking tip was 10%")
        elif (average_cook_time + standard_deviation) <= actual_cook_time and actual_cook_time <= (average_cook_time + 2*standard_deviation):
            print(f"{food_cooking} was slightly overcooked and cooking tip was 0%")
        elif (average_cook_time + 2*standard_deviation) < actual_cook_time:
            print(f"{food_cooking} was very overcooked and cooking tip was -100%")
    else:
        print("invalid choice")

