import math
def print_bmi(weight,height):
    h=height/100
    bmi=(weight/(math.pow(h,2)))
    print('your bmi is',(bmi))
weight=float(input('Please enter your weight '))
height=float(input('Please enter your height '))
print_bmi(weight,height)
