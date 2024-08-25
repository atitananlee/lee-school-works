h=int(input('ENTER HEIGHTS (INT>2) '))
b=2*h-1
s='★'
tallleft=(h-1)
tallright=h
if h<=2:
    print('invalid num please enter more than 2 integer')
elif h>2:
    for x in range (h-1,0,-1):
        print('','★'+'★')
    print('★'*b)
