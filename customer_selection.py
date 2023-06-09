#R.3

''' 09/06/23 Comments
Similar to get_menu, the user inputs their own menu or uses the default one provided, and picks a meal that they wish
to consume.

The user can only pick a meal from the list inputted / provided otherwise an error message will return, informing
them of their invalid choice. Otherwise, a message will indict their meal is being prepared.


'''

input_food = input() #get food details from user
dictionaries = {}
options = [] #this will store the food dictionaries
full_stop = False #false until user inputs "."

#if user inputs '.' first, put default foods into options 
if input_food == '.':
    full_stop = True
    options = [
    {'name': 'Budda Bowl (vg)', 'sell_for': 25, 'cost_to_make': 20, 'cook_time': 10, 'cook_time_stdev': 3}, 
    {'name': 'Eye Fillet Steak', 'sell_for': 55, 'cost_to_make': 25, 'cook_time': 7, 'cook_time_stdev': 1}, 
    {'name': 'Spaghetti Bolognese', 'sell_for': 30, 'cost_to_make': 22, 'cook_time': 40, 'cook_time_stdev': 5}, 
    {'name': 'Pad Thai (seafood)', 'sell_for': 22, 'cost_to_make': 17, 'cook_time': 30, 'cook_time_stdev': 1}
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

#add menu_number as a key in each food dictionary
menu_number = 0
for i in options:    
    name = i["name"]
    sell_for = float(i["sell_for"])
    cost_to_make = float(i["cost_to_make"])
    cook_time = float(i["cook_time"])
    cook_time_stdev = float(i["cook_time_stdev"])
    menu_number += 1

#input a meal number and (if valid) print which meal is cooking 
if full_stop == True:
    meal_selection_number = input() # get chosen meal number from user
    if meal_selection_number.isdigit() == False or int(meal_selection_number) <= 0: # if input contains something other than digits, print "invalid choice"
        print("invalid choice")
    elif int(meal_selection_number) <= len(options): #Check to see if the input integer is within range of the food list
        meal_selection_number = int(meal_selection_number)
        food_cooking = options[meal_selection_number - 1]['name']#if meal_selection_number = 1, this accesses options[0] and that food dictionary's 'name' entry
        print(f"now cooking {food_cooking}") #prints out the food being cooked if valid
    else:
        print("invalid choice")



