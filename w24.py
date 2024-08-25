import csv
with open('23.csv') as f:
    title=csv.DictReader(f,fieldnames=['Restaurant','Starting Price'])
    for k in title:
        if k['Starting Price']<300:
            a=k['Restaurant']
            b=k['Starting Price']
            print(f'Restaurant that Cheaper than 300 is {a} {b}')   