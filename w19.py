def print_Calculator(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return  a*b
    elif op=='/':
        return a/b
a=float(input('please enter num 1: '))
b=float(input('please enter num 2: '))
op=str(input('please input operator: '))
result=print_Calculator(a,b,op)\

print(result)
