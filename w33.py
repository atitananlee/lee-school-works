from tkinter import*
root= Tk()

root.config(bg='lightgrey')
root.title('Science Test')
root.option_add("font*",'Kanit 30')
root.config(bg='white')

def finish():
     global count
     root.destroy()
     root2=Tk()
     root2.title('รายงานผลคะเเนนทั้งหมด')
     root2.option_add("*font",'PSL-omyim 30')
     Label(root2,text=f'total point : {count}',fg='purple',width=34).pack()
     root2.mainloop()
def countclick():
     global count
     count +=1
     totalpt.set(f'Total point : {count}')

pt1= PhotoImage(file='north.png')
pt2= PhotoImage(file='east.png')
pt3= PhotoImage(file='west.png')
pt4= PhotoImage(file='south.png')

label1  = Label(text='ดวงอาทิตย์ขึ้นทางทิศอะไร ?',fg='black',font=100,bg='yellow')
label1.grid(row=0,column=0,sticky='we',ipady=25,columnspan=4,pady=2)
label2  = Label(text='ให้นักเรียนเลือกคำตอบด้านล่าง',fg='black',font=100,bg='lightblue')
label2.grid(row=1,column=0,sticky='we',ipady=25,columnspan=4,pady=2)

button1 = Button(text='ก.ทิศเหนือ',image=pt1,compound=TOP,fg='red',bg='orange')
button1.grid(row=3,column=0,ipadx=50,ipady=50,padx=2)
button2 = Button(text='ข.ทิศตะวันออก',image=pt2,compound=TOP,fg='red',bg='orange',command=countclick)
button2.grid(row=3,column=1,ipadx=50,ipady=50,padx=2)
button3 = Button(text='ค.ทิศตะวันตก',image=pt3,compound=TOP,fg='red',bg='orange')
button3.grid(row=3,column=2,ipadx=50,ipady=50,padx=2)
button4 = Button(text='ง.ทิศใต้',image=pt4,compound=TOP,fg='red',bg='orange')
button4.grid(row=3,column=3,ipadx=50,ipady=50,padx=2)

label3 =Label(text='TOTAL POINT : 0',fg='purple',font=100,bg='lightgrey')
label3.grid(row=4,column=0,sticky='we',ipady=25,columnspan=4,pady=2)
button5 = Button(text='finish',fg='blue',font=100,bg='lightgrey')
button5.grid(row=5,column=0,sticky='we',ipady=25,columnspan=4,pady=2)

totalpt=StringVar()
totalpt.set('Total point : 0')
count=0
def finish():
     global count
     root.destroy()
     root2=Tk()
     root2.title('รายงานผลคะเเนนทั้งหมด')
     root2.option_add("*font",'PSL-omyim 30')
     Label(root2,text=f'total point : {count}',fg='purple',width=34).pack()
     root2.mainloop()
btpt= Button(textvariable=totalpt,fg='purple',command=finish)
btpt.grid(row=5,columnspan=6,sticky=NSEW)
btfinish= Button(text='Finish',fg='blue',command=finish)
btfinish.grid(row=6,column=0,columnspan=5)



root.mainloop()