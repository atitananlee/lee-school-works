# work
score=int(input('please enter your total score (0-100)  '))
if score >100 or score <0:
    print('please enter number 0-100 only ')
elif score >=80:
    print('your total grade is 4 ')
elif score >=75:
    print('Your total grade is 3.5')
elif score >=70:
     print('Your total grade is 3')
elif score >=65:
     print('Your total grade is 2.5')
elif score >=60:
     print('Your total grade is 2')
elif score >=55:
     print('Your total grade is 1.5')
elif score >=50:
     print('Your total grade is 1')
elif score <50:
     print('Your total grade is 0')