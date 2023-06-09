#R.1-9

''' 09/06/23 Comments
This final section is a combination of all previous functions and tasks into one. With the addition of
adding extra functions to successfully implement the random chance of tips.

The use of dictionaries and the combination in a return string statement is what the main focus of this
code was. Attempting to get a user input for their personal or default menu list. Followed up by cooking their
selected menu item.

The code would only allow for 3 chances for the menu item to be cooked. After determining the calculation of
average_cook_time - / + stdev_cook_time, where this value becomes the final_cooking_tip which is used to determine
the total tip value. After a randomised tip chance and value is determined.

All of the functions produce a key value dependent on user selection. Once this selection has been made, through a series
of pre-determined calculations, alongside randomised values, a statement is returned at the end. Depicting whether
or not a meal was successfully produced, how long it took in comparison to the average time it should take, as well as
the tip it received. Before finally summarising the total profit the meal would have made.

'''

import random 
#--------------------------------------------------------------------------------------------------------------
# R.1 function
def get_meals_list_from_user() -> list:
    '''Returns a list named `options`, containing food dictionaries'''
    options = [] #this will store the food dictionaries
    input_food = input() #get food details from the user
    
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
            
    return options

#--------------------------------------------------------------------------------------------------------------
# R.2 function
def display_menu(options: list):
    '''Prints out a menu with food`name`, how much it would `sell_for`, `cost_to_make` and `cook_time`'''
    menu_number = 0

    for i in options:    
        #Get the menu number for each food in options
        name = i["name"]
        sell_for = (i["sell_for"])
        cost_to_make = (i["cost_to_make"])
        cook_time = (i["cook_time"])
        cook_time_stdev = (i["cook_time_stdev"])
        menu_number += 1
     
        print(f"{menu_number}. Name:{name} Sells:${sell_for} Costs:${cost_to_make} Takes:{cook_time} mins")
#--------------------------------------------------------------------------------------------------------------
# R.3 function 
def validate_user_choice(options: list, users_input: str) -> bool:
    '''Returns whether user choice is valid (True) or invalid (False)'''
    if users_input.isdigit() == False or int(users_input) <= 0 or int(users_input) >= 5: # if input contains something other than digits, print "invalid choice"
        return False
    elif int(users_input) <= len(options): #Check to see if the input integer is within range of the food list
        users_input = int(users_input)
        food_cooking = options[users_input - 1] #if users_input = 1, this accesses options[0] and that food dictionary's 'name' entry
        return True #prints out the food being cooked if valid
    else:
        return False
#--------------------------------------------------------------------------------------------------------------
# R.5 functions
def classify_cook_time(average_cook_time: float, stdev_cook_time: float, actual_cook_time: float) -> str: 
    '''Compares average and actual cook time; returns how cooked the food is'''
    
    #converts the variables into floats for calculation
    stdev_cook_time = float(stdev_cook_time) 
    average_cook_time = float(average_cook_time)
    actual_cook_time = float(actual_cook_time)
    
    # Compare actual cook time to mean and standard deviation, return cooking classification
    if actual_cook_time < average_cook_time - 2*stdev_cook_time:
        return("very undercooked")
    elif (average_cook_time - 2 * stdev_cook_time) <= actual_cook_time and actual_cook_time <= (average_cook_time - stdev_cook_time):
        return("slightly undercooked")
    elif (average_cook_time - stdev_cook_time) < actual_cook_time and actual_cook_time < (average_cook_time + stdev_cook_time):
        return("well cooked")
    elif (average_cook_time + stdev_cook_time) <= actual_cook_time and actual_cook_time <= (average_cook_time + 2*stdev_cook_time):
        return("slightly overcooked")
    elif (average_cook_time + 2*stdev_cook_time) < actual_cook_time:
        return("very overcooked")
    else:
        return("invalid choice")

def get_cooking_tip(classification: str, base_tip: int) -> int: 
    ''' Returns the cooking tip depending on how well-cooked the food is'''
    if classification == 'very undercooked':
        final_cooking_tip = -100
        return final_cooking_tip
    elif classification == 'slightly undercooked':
        final_cooking_tip = 0
        return final_cooking_tip
    elif classification == 'well cooked':
        final_cooking_tip = base_tip
        return final_cooking_tip
    elif classification == 'slightly overcooked':
        final_cooking_tip = 0
        return final_cooking_tip
    elif classification == 'very overcooked':
        final_cooking_tip = -100
        return final_cooking_tip

#--------------------------------------------------------------------------------------------------------------
# R.7 function
def random_tip_compute(tip_chance: float, base_tip_value: float, random_comparison: float) -> float:
    '''Returns tip paid based on base_tip_value and chance'''
    
    # converts the variables into floats for calculation
    tip_chance = float(tip_chance) 
    base_tip_value = float(base_tip_value) 
    random_comparison = float(random_comparison) 
     
    # compare random_comparison to tip_chance, output correct tip and 'actual cooking time'
    if 0 < tip_chance < 0.5:
        if random_comparison < tip_chance:
            tip_paid = base_tip_value
            return(tip_paid)
        elif random_comparison > (1 - tip_chance):
            tip_paid = - base_tip_value
            return(tip_paid)
        else:
            tip_paid = 0
            return(tip_paid)
    return 0
#--------------------------------------------------------------------------------------------------------------
# R.8 Profit Calculation; R.6 Retry Cooking
def order(options: list) -> float:
    '''Print all customer order details, return profit'''
    display_menu(options)
    users_input = input('Pick a meal by inputting the number your food corresponds to.\n') #get meal number from user
    while validate_user_choice(options, users_input) == False: # makes sure the user puts in a valid option for the meal
        users_input = input('invalid choice.\n')
    if validate_user_choice(options, users_input) == True: 
        #retrieve meal name, cook time average and standard deviation
        food_cooking = options[int(users_input) - 1] 
        name_of_food = food_cooking['name']
        average_cook_time = food_cooking['cook_time'] 
        stdev_cook_time = food_cooking['cook_time_stdev']

        cooking_attempts_left = 3 
        cooking_attempt_successful = False
        accumulated_cooking_cost = 0
        final_selling_price = 0
        while cooking_attempts_left > 0 and cooking_attempt_successful == False:
            actual_cook_time = round(random.gauss(average_cook_time, stdev_cook_time), 2) #generate actual cook time
            classification = classify_cook_time(average_cook_time,stdev_cook_time, actual_cook_time)
            base_tip = 10  # base tip assumed to be 10% of selling price
            final_cooking_tip = round(get_cooking_tip(classification, base_tip))
            random_number = round(random.random(), 2)
            if random_number <= 0.1:
                random_tip = 5 #random tip value assumed to be 5% of selling price
            elif random_number >= 0.9:
                random_tip = -5
            else:
                random_tip = 0
            total_tip = (final_cooking_tip/100) + (random_tip/100)# convert tips to decimals, add them together 
            if total_tip < -1:
                total_tip = -1
            selling_price = (total_tip + 1) * food_cooking['sell_for']
            profit = selling_price - food_cooking['cost_to_make']
            if classification == "very overcooked" or classification ==  "very undercooked":
                print(classification)
                cooking_attempts_left -= 1
            else:
                cooking_attempt_successful = True
                cooking_attempts_left -= 1
            print(f"now cooking {name_of_food}\n{name_of_food} was {classification} ({actual_cook_time:.2f} vs {average_cook_time:.2f} mins)\ncooking tip was {final_cooking_tip} random tip was {random_tip} the random value being {random_number:.2f}\nfinal selling price was ${selling_price:.2f}\nfor a profit of ${profit:.2f}")

            final_selling_price = final_selling_price + selling_price
            accumulated_cooking_cost += food_cooking['cost_to_make']

        final_profit = final_selling_price - accumulated_cooking_cost

        if cooking_attempts_left == 2:
            print(f'overall, the profit for this meal was ${final_profit:.2f}')
        elif cooking_attempts_left == 1:
            print(f'overall, the profit for this meal was ${final_profit:.2f}')
        elif cooking_attempts_left == 0:
            print(f'giving up after 3 failed attempts \noverall, the profit for this meal was ${final_profit:.2f}')
        return final_profit
#---------------------------------------------------------------------------------------------------------------------------------------------------------
# R.9 Profit Calculation - ordering for multiple people

def order_for_x_people(X: int) -> float: #X = number of customers
    '''Returns overall profit from multiple customer orders'''
    running_profit = 0
    options = get_meals_list_from_user()
    for i in range(X):
        running_profit += order(options)
        print(f'running profit ${running_profit:.2f} ')
    print(f"After serving meals to {X} people, we made a profit of ${running_profit:.2f}")
    return running_profit

if __name__ == '__main__': 
    order_for_x_people(1)
   
