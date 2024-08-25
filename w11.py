print('Hello welcome to Taotys store')
ismembers=str(input('already have Taotys members ?  '))
bill=float(input('please enter your total bills  '))
if ismembers =='yes':
    print(bill)
    print('Please sign in for our memberships')
    if bill >=500:
        print('Congrats you got 5% Discount your total bills is',bill-(bill**5/100))
elif bill >=1000:
    print('Congrats you got 10% Discount your total bills is',bill-(bill**10/100))
elif bill >=1500:
    print('Congrats you got 15% Discount your total bills is',bill-(bill**15/100))
print('Thank you for shopping at Taotys store')