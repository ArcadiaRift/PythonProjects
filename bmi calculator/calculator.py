#! python3
# The BMI calculator will take ur height and weight and determine whether you're underweight, normal, overweight, or obese

import time #import the time module to use the .sleep method, which will allow me to delay print statements to make it easier to follow
print('Welcome to the BMI Calculator!')
time.sleep(1)
print('This program will help determine whether you\'re underweight, normal, overweight, or obese')
time.sleep(1)
print('Let\'s begin!')
time.sleep(1)
weight = float(input('Enter your weight in kilograms: ')) #ask the user to input their weight
height = float(input('Now enter your height in meters: ')) #ask the user to input their height. The float type is more convenient for weight and height as they aren't always integers

BMI = weight / (height ** 2) #use the BMI formula to calculate the BMI and store it in a variable called 'BMI'

if BMI < 18.5: #i.e. if the user is underweight
    print('You are underweight!')
    print('You need to gain at least ' + str(round(18.5 * (height ** 2) - weight)) + 'kg to become normal.') #determine the difference needed for the BMI to be in the 'normal' range. this concenpt is reused in lines 21 and 24
elif BMI < 29.9 and BMI > 25: #i.e. if the user is overweight
    print('You are overweight!')
    print('You need to lose at least ' + str(round(weight - 24.9 * (height ** 2))) + 'kg to become normal.')
elif BMI > 30: #i.e. if the user is obese. 
    print('You are obese!')
    print('You need to lose at least ' + str(round(weight - 24.9 * (height ** 2))) + 'kg to become normal.')
else: #if the user is not obese,overweight, or underweight, then they have to be in the 'normal' range of the BMI scale
    print('Your weight is normal!')

time.sleep(1)
print('Remember, this is based on the BMI scale, which might not necessarily indicate your overall fitness levels. There might be other underlying reasons that determine your weight and fitness l.')leve