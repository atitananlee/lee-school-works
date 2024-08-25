def demoline():
    f = open('name.txt')
    line=f.readlines()
    data=[]
    for entry in line:
        data.append(entry.split('/n'))
    for name,score in data:
        if int(score)>60:
            print(name,score)
    else:
        print(name)
    f.close()
demoline()


