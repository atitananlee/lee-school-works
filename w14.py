menu = {'taotys fried chicky':'299฿','taotys pad phed':'199฿','somtam taoty':'175฿','taotys burger':'149฿',}
order=str(input('please enter your order menu  '))
if order in menu.keys():
    print('ัyour order is',order,'the total price is',menu[order])

