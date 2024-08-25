stuid= input('Enter your student id :  ')
physic=input('Enter your physic point :  ')
chemistry=input('Enter your chemistry point :  ')
biology=input('Enter your biology point :  ')
f=open('inform.txt','r',encoding='utf-8')
# f.writelines('%s,%s,%s,%s\n'%(stuid,physic,chemistry,biology))
a = f.readlines()
data=[]
for entry in a:
        data.append(entry.strip())
print()
    