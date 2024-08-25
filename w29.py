import numpy as np
day= ['mon','tue','wed','turs','fri','sun']
pricingfood= np.array([25,30,45])
daily=np.array([[75,120,70,90,80],
                [80,90,100,70,50],
                [50,45,70,65,50]])
#Q1Print
print('ขายได้วันละ (หน่วยเป็นจาน) :')
print(day)
print(np.sum(daily,axis=0))
#Q2Print
at=np.sum(daily[0])
bt=np.sum(daily[1])
ct=np.sum(daily[2])
listmax=[at,bt,ct]
mmm=max(listmax)
print('ขายข้าวแกงได้',np.sum(daily[0]),'บาท')
print('ขายข้าวผัดได้',np.sum(daily[1]),'บาท')
print('ขายสุกี้น้ำได้',np.sum(daily[2]),'บาท')
#Q3Print
if mmm==at:
    print('ข้าวแกง BESTSELLER ขายได้',mmm,'bath')
elif mmm==bt:
    print('ข้าวผัด BESTSELLER ขายได้',mmm,'bath')
elif mmm==ct:
    print('สุกี้วอเตอร์ BESTSELLER ขายได้',mmm,'bath')