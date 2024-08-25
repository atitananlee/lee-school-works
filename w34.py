from tkinter import*
root= Tk()

root.geometry='500x1000'
root.config(bg='white')
root.title('Cherly korea cosmetic')
root.option_add("font*",'Kanit 30')


def countclick_Roamnd():
     global count
     count +=299
def countclick_cliocu():
    global  count
    count +=1090
def countclick_cliopl():
    global count
    count +=1299
def countclick_laneg():
    global count
    count +=1699
     


pt1= PhotoImage(file='111.png')
pt2= PhotoImage(file='222.png')
pt3= PhotoImage(file='333.png')
pt4= PhotoImage(file='444.png')

labelname=Label(text='Cherly Korea Cosmetic',fg='white',font=50,bg='pink')
labelname.grid(row=0,column=0,sticky='we',ipady=25,columnspan=4,pady=2)
labelSLOGAN=Label(text='Authentic from seoul to you',fg='white',font=50,bg='pink')
labelSLOGAN.grid(row=1,column=0,sticky='we',ipady=25,columnspan=4,pady=2)
label_romand=Button(text='Romand Juicy lasting tint \n 299฿',image=pt1,compound=TOP,fg='white',font=100,bg='grey',command=countclick_Roamnd)
label_romand.grid(row=2,column=0,ipadx=15,ipady=15,padx=2)
label_clio=Button(text='  Clio glow cushion   \n 1090฿',image=pt2,compound=TOP,fg='white',font=100,bg='grey',command=countclick_cliocu )
label_clio.grid(row=2,column=1,ipadx=15,ipady=15,padx=2)
label_cliopl=Button(text='     Clio pro eyepalette     \n 1299฿',image=pt3,compound=TOP,fg='white',font=100,bg='grey',command=countclick_cliopl)
label_cliopl.grid(row=3,column=0,ipadx=15,ipady=15,padx=2)
label_laneg=Button(text='Laneige Water bank \n 1699฿',image=pt4,compound=TOP,fg='white',font=100,bg='grey',command=countclick_laneg)
label_laneg.grid(row=3,column=1,ipadx=15,ipady=15,padx=2)


totalmn=StringVar()
totalmn.set('Total money : 0')
count=0
def finish():
     global count
     root.destroy()
     root2=Tk()
     root2.title('RECIEPT OF THE BEAUTY')
     root2.option_add("*font",'PSL-omyim 30')
     Label(root2,text=f'TOTAL : {count}',fg='purple',width=34).pack()
     root2.mainloop()
btpt= Button(textvariable=totalmn,fg='purple',command=finish)
btpt.grid(row=6,columnspan=6,sticky=NSEW)
btfinish= Button(text='Finish',fg='blue',command=finish)
btfinish.grid(row=7,column=0,columnspan=6)

totallist=StringVar()
totallist.set('all of the list of order : 0')
count=0
def finish():
     global count
     root2=Tk()
     root2.title('All of the list of order : 0 ')
     root2.option_add("*font",'PSL-omyim 30')
     Label(root2,text=f'List Total : {count}',fg='purple',width=34).pack()
     root2.mainloop()




root.mainloop()