from tkinter import *
import numpy as np
root= Tk()

root.geometry='500x100'
root.config(bg='white')
root.title('Cherly korea cosmetic')
root.option_add("font*",'Kanit 30')
root.grid_columnconfigure(0, weight=1, uniform="fred")
root.grid_columnconfigure(1, weight=1, uniform="fred")


global odlist

melist = np.array(["Romand Juicy lasting tint","Clio glow cushion","Clio pro eyepalette","Laneige Water bank"])
prlist = np.array([299,1090,1299,1699])


def pd1():
    odlist[0] += 1
def pd2():
    odlist[1] += 1
def pd3():
    odlist[2] += 1
def pd4():
    odlist[3] += 1
def clear():
    global odlist
    odlist= np.array([0,0,0,0])
def checko():
    root.destroy()
    root2 = Tk()

    root2.geometry("450x450")
    root2.configure(background="pink")

    laone = Label(text = "Cherly Korea cosmetic",font = ("Kanit",25), fg="white", bg="pink")
    laone.pack(side=TOP,fill=BOTH)

    lato = Label(text=f"{melist[0]} {odlist[0]} piece \n{melist[1]}  {odlist[1]} piece \n{melist[2]} {odlist[2]} piece \n{melist[3]}  {odlist[3]} piece", font = ("Arial 20"), fg='white',bg='pink')
    lato.place(relx = 0.07 , rely=0.2)

    latt = Label(text=f"{prlist[0]}฿ x {odlist[0]}\n{prlist[1]}฿ x {odlist[1]}\n{prlist[2]}฿ x {odlist[2]}\n{prlist[3]}฿ x {odlist[3]}\n total is  {sum(prlist*odlist)}฿", font = ("Arial",20), fg='white',bg='pink')
    latt.place(relx = 0.34 , rely=0.472)
    
    lattk =Label(text=f'thank you for purchase with us\n ',fg='white',font=70,bg='grey')

clear()
pt1= PhotoImage(file='111.png')
pt2= PhotoImage(file='222.png')
pt3= PhotoImage(file='333.png')
pt4= PhotoImage(file='444.png')

labelname=Label(text='Cherly Korea Cosmetic',fg='white',font=50,bg='pink')
labelname.grid(row=0,column=0,ipady=25,columnspan=4,pady=2,sticky="nesw")
labelslo=Label(text='Authentic from seoul to you',fg='white',font=50,bg='pink')
labelslo.grid(row=1,column=0,ipady=25,columnspan=4,pady=2,sticky="nesw")
label_romand=Button(text='Romand Juicy lasting tint \n 299฿',image=pt1,compound=TOP,fg='white',font=70,bg='grey',command=pd1)
label_romand.grid(row=2,column=0,ipadx=20,ipady=20,padx=2,sticky="nesw")
label_clio=Button(text='Clio glow cushion \n 1090฿',image=pt2,compound=TOP,fg='white',font=70,bg='grey',command=pd2)
label_clio.grid(row=2,column=1,ipadx=20,ipady=20,padx=2,sticky="nesw")
label_cliopl=Button(text='Clio pro eyepalette \n 1299฿',image=pt3,compound=TOP,fg='white',font=70,bg='grey',command=pd3)
label_cliopl.grid(row=3,column=0,ipadx=20,ipady=20,padx=2,sticky="nesw")
label_laneg=Button(text='Laneige Water bank \n 1699฿',image=pt4,compound=TOP,fg='white',font=70,bg='grey',command=pd4)
label_laneg.grid(row=3,column=1,ipadx=20,ipady=20,padx=2,sticky="nesw")
lebel_check=Button(text='CheckBills',fg='white',font=50,bg='pink',command=checko)
lebel_check.grid(row=4,column=0,ipady=25,columnspan=1,pady=2,sticky="nesw")
lebel_reset=Button(text='Reset',fg='white',font=50,bg='pink',command=clear,)
lebel_reset.grid(row=4,column=1,ipady=25,columnspan=1,pady=2,sticky="nesw")

root.mainloop()









