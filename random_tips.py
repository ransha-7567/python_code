# R.4. and R.7

''' 09/06/23 Comments
A section of code heavily dependent on the use of random. If a specific value falls within a certain threshold,
return a specific string along with the actual value produced from a randomised calculation. Which was based on
the use of 2 user inputted values.

'''

import random

# Gets cook time average and standard deviation from user, formats them
average_cook_time,cook_time_stdev = input("").split(',') 
average_cook_time = float(average_cook_time) 
cook_time_stdev = float(cook_time_stdev) 

# Generates random 'actual cooking time'
actual_cook_time = random.gauss(average_cook_time, cook_time_stdev) 

# Generates random frequency to determine if tip should be paid
probability = random.random() 

# Check if 'probability' meets the specific tip thresholds, output correct tip and 'actual cooking time'
if probability >= 0.9:
    print(f"Actual cooking time was {actual_cook_time} and the tip paid was -5%")
elif 0.1 < probability < 0.9:
    print(f"Actual cooking time was {actual_cook_time} and the tip paid was 0%")
elif probability <= 0.1:
    print(f"Actual cooking time was {actual_cook_time} and the tip paid was 5%")

