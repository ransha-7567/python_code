#R.1

''' 09/06/23 Comments
Manually input your own meal and have it return the total details of said meal. Take for example to following
Inputting the following -
Budda Bowl (vg), 25.0, 20.0, 10.0, 3.0
.

Would return the meal in this particular format -
{'name': 'Budda Bowl (vg)', 'sell_for': 25.0, 'cost_to_make': 20.0, 'cook_time': 10.0, 'cook_time_stdev': 3.0},

'''

options = [] #this will store all the food dictionaries
dictionaries = {} #this initializes the food dicionaries (one per option)

#get food details, save each as a dictionary, and store it in options
full_stop = False 
food_number = 0 
while full_stop == False: #iterate per food option until user inputs '.'
    input_food = input() 
    if input_food == '.':
        full_stop = True
    else:
        input_list = input_food.split(',')
        dictionaries["food" + str(food_number)] = {
            "name": input_list[0],
            "sell_for": float(input_list[1]), 
            "cost_to_make": float(input_list[2]),
            "cook_time": float(input_list[3]),
            "cook_time_stdev": float(input_list[4])
            }
        options.append(dictionaries["food" + str(food_number)]) 

        food_number += 1 

print(options)

