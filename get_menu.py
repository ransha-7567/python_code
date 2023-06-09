#R.2 

''' 09/06/23 Comments
If user inputs '.' the code will return a default menu list.

Whereas if the user wishes to, they can personally input a series of menu items, and after this, enter a '.'
to finalise the menu. To which it will return a menu list containing all the meals they inputted.

'''

input_food = input() #get food details from user
options = [] #this will store the food dictionaries
full_stop = False #false until user inputs "."

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

#add menu_number as a key in each food dictionary, then print food details
menu_number = 0
for i in options:    
    name = i["name"]
    sell_for = float(i["sell_for"])
    cost_to_make = float(i["cost_to_make"])
    cook_time = float(i["cook_time"])
    cook_time_stdev = float(i["cook_time_stdev"])
    menu_number += 1

    print(f"{menu_number}. Name:{name} Sells:${sell_for} Costs:${cost_to_make} Takes:{cook_time} mins") 


