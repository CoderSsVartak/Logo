from tkinter import *
import time

import tkinter as tk
global result
result=[]


win = Tk()




def main_screen1():
    win.withdraw()
    global win1
    win1=Toplevel(win)
    win1.withdraw()
    win1 = Tk(className="Game Window")
    win1.title("TRUTH OR FLUKE.....")
    win.geometry("300x250")
    win.withdraw()

    Label(win1,text="GUESS THE LOGOS..!!",width="50", height="2", font=("Arial Bold",25)).pack()  
    Label(win1,text="Welcome to The Game..",width="50", height="4", font=("Calibri",20)).pack(padx=4,pady=5)  
    Button(win1,text="START GAME", height="3", width="13",command=actl).pack()


def actl():
    win1.destroy()
    global addimg1
    addimg1 = Toplevel(win)
    addimg1.title("GAME")
    addimg1.geometry("300x250")

    L1 = Label(addimg1,text = "1.Guess which logo it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg1,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="img1.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v=IntVar()
    def clicked():
        
        
        if v.get() == 1:
            L2 = Label(addimg1,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg1,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

        if v.get()==1:
            result.append(1)
        else:
            result.append(0)
    
         

    r1=Radiobutton(addimg1, text="google",padx=20,variable=v,value=3,command=clicked).pack(anchor=tk.W)
    r2=Radiobutton(addimg1, text="gmail",padx=20,variable=v,value=2,command=clicked).pack(anchor=tk.W)
    r3=Radiobutton(addimg1, text="yahoo",padx=20,variable=v,value=1,command=clicked).pack(anchor=tk.W)    
    r4=Radiobutton(addimg1, text="yahee",padx=20,variable=v,value=4,command=clicked).pack(anchor=tk.W)
    
 
        
    Button(addimg1, text="NEXT", width=10, height=1,command=actl2).pack()


def actl2():
    addimg1.destroy()
    global addimg2
    addimg2 = Toplevel(win)
    addimg2.title("GAME")
    addimg2.geometry("300x250")

    L1 = Label(addimg2,text = "2.Guess which logo it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg2,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="img2.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v2=IntVar()
    def clicked2():
        
        
        if v2.get() == 1:
            L2 = Label(addimg2,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg2,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

        if v2.get()==1:
            result.append(1)
        else:
            result.append(0)
   
    
    v2=tk.IntVar()
    Radiobutton(addimg2, text="mozilla firefox",padx=20,variable=v2,value=1,command=clicked2).pack(anchor=tk.W)
    Radiobutton(addimg2, text="mozilla foxfire",padx=20,variable=v2,value=2,command=clicked2).pack(anchor=tk.W)
    Radiobutton(addimg2, text="fire browser",padx=20,variable=v2,value=3,command=clicked2).pack(anchor=tk.W)    
    Radiobutton(addimg2, text="chrome",padx=20,variable=v2,value=4,command=clicked2).pack(anchor=tk.W)
    
    
        
    Button(addimg2, text="NEXT", width=10, height=1,command=actl3).pack()


def actl3():
    addimg2.destroy()
    global addimg3
    addimg3 = Toplevel(win)
    addimg3.title("GAME")
    addimg3.geometry("300x250")

    L1 = Label(addimg3,text = "3.Guess which logo it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg3,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="img3.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v3=IntVar()
    def clicked3():
        
        
        if v3.get() == 1:
            L2 = Label(addimg3,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg3,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

        if v3.get()==1:
            result.append(1)
        else:
            result.append(0)
    
   
    Radiobutton(addimg3, text="webpedia",padx=20,variable=v3,value=4,command=clicked3).pack(anchor=tk.W)
    Radiobutton(addimg3, text="technodia ",padx=20,variable=v3,value=2,command=clicked3).pack(anchor=tk.W)
    Radiobutton(addimg3, text="vikipedia",padx=20,variable=v3,value=3,command=clicked3).pack(anchor=tk.W)    
    Radiobutton(addimg3, text="wikipedia",padx=20,variable=v3,value=1,command=clicked3).pack(anchor=tk.W)

        
    Button(addimg3, text="NEXT", width=10, height=1,command=actl4).pack()


def actl4():
    addimg3.destroy()
    global addimg4
    addimg4 = Toplevel(win)
    addimg4.title("GAME")
    addimg4.geometry("300x250")

    L1 = Label(addimg4,text = "4.Guess which logo it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg4,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="img4.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v4=IntVar()
    def clicked4():
        
        
        if v4.get() == 1:
            L2 = Label(addimg4,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg4,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

            
        if v4.get()==1:
            result.append(1)
        else:
            result.append(0)
   
    Radiobutton(addimg4, text="pixar",padx=20,variable=v4,value=2,command=clicked4).pack(anchor=tk.W)
    Radiobutton(addimg4, text="dreamworks",padx=20,variable=v4,value=1,command=clicked4).pack(anchor=tk.W)
    Radiobutton(addimg4, text="paramound",padx=20,variable=v4,value=3,command=clicked4).pack(anchor=tk.W)    
    Radiobutton(addimg4, text="illumination",padx=20,variable=v4,value=4,command=clicked4).pack(anchor=tk.W)
    

        
    Button(addimg4, text="NEXT", width=10, height=1,command=actl5).pack()


def actl5():
    addimg4.destroy()
    global addimg5
    addimg5 = Toplevel(win)
    addimg5.title("GAME")
    addimg5.geometry("300x250")

    L1 = Label(addimg5,text = "5.Guess which logo it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg5,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="img5.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v5=IntVar()
    def clicked5():
        
        
        if v5.get() == 1:
            L2 = Label(addimg5,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg5,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()
   
        if v5.get()==1:
            result.append(1)
        else:
            result.append(0)
    
    Radiobutton(addimg5, text="warner bros. pictures",padx=20,variable=v5,value=1,command=clicked5).pack(anchor=tk.W)
    Radiobutton(addimg5, text="wright brothers",padx=20,variable=v5,value=2,command=clicked5).pack(anchor=tk.W)
    Radiobutton(addimg5, text="disney",padx=20,variable=v5,value=3,command=clicked5).pack(anchor=tk.W)    
    Radiobutton(addimg5, text="pixar",padx=20,variable=v5,value=4,command=clicked5).pack(anchor=tk.W)

  
        
    Button(addimg5, text="NEXT", width=10, height=1,command=actl6).pack()


    
    
    
    
    
     
    
def actl6():
    addimg5.destroy()
    global addimg6
    addimg6 = Toplevel(win)
    addimg6.title("Game")
    addimg6.geometry("350x200")

    
    
    L2 = Label(addimg6,text = "6.Guess which logo it is..??",width="50", height="3", font=("Calibri",13))
    L2.pack()
    canvas1=Canvas(addimg6,width=300, height=300)
    canvas1.pack()
    img1=PhotoImage(file="img6.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v6=IntVar()
    def clicked6():
        
        
        if v6.get() == 1:
            L2 = Label(addimg6,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg6,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()


        if v6.get()==1:
            result.append(1)
        else:
            result.append(0)


     
    Radiobutton(addimg6, text="twity",padx=20,variable=v6,value=3,command=clicked6).pack(anchor=tk.W)
    Radiobutton(addimg6, text="bluebird",padx=20,variable=v6,value=2,command=clicked6).pack(anchor=tk.W)
    Radiobutton(addimg6, text="twitter",padx=20,variable=v6,value=1,command=clicked6).pack(anchor=tk.W)    
    Radiobutton(addimg6, text="tweety",padx=20,variable=v6,value=4,command=clicked6).pack(anchor=tk.W)    
    Button(addimg6, text="NEXT", width=10, height=1,command=actl7).pack()




def actl7():
    addimg6.destroy()
    global addimg7
    addimg7 = Toplevel(win)
    addimg7.title("Game")
    addimg7.geometry("350x200")

    L2 = Label(addimg7,text = "7.Guess which logo it is..??",width="50", height="3", font=("Calibri",13))
    L2.pack()
    canvas1=Canvas(addimg7,width=300, height=300)
    canvas1.pack()
    img1=PhotoImage(file="img7.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v7=IntVar()
    def clicked7():
        
        
        if v7.get() == 1:
            L2 = Label(addimg7,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg7,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()


        if v7.get()==1:
            result.append(1)
        else:
            result.append(0)


     
    Radiobutton(addimg7, text="tago bell",padx=20,variable=v7,value=3,command=clicked7).pack(anchor=tk.W)
    Radiobutton(addimg7, text="taco bell",padx=20,variable=v7,value=1,command=clicked7).pack(anchor=tk.W)
    Radiobutton(addimg7, text="tinker bell",padx=20,variable=v7,value=2,command=clicked7).pack(anchor=tk.W)    
    Radiobutton(addimg7, text="tiny bell",padx=20,variable=v7,value=4,command=clicked7).pack(anchor=tk.W)    
    Button(addimg7, text="NEXT", width=10, height=1,command=scorel).pack()
    
def scorel():
    win.destroy()
    root=Tk()
    c=Canvas(root,width=500,height=500,bg="black")
    s=c.create_oval(200,200,300,300,fill="yellow")
    cr=c.create_polygon(500,50,460,50,460,500,500,500,fill="green")
    t=0
    for i in range(9):
        cr=c.create_polygon(0,50+t,0,100+t,50,75+t,fill="red")
        t=t+50
    c.pack()
    a=1
    b=1
    print(result)
    for i in result:
        if i==1:
            if a==1:
                c.move(s,25,0)
                c.itemconfig(s,fill="orange")
                root.update()
                root.after(500)
            if a==2:
                c.move(s,25,0)
                c.itemconfig(s,fill="red")
                root.update()
                root.after(500)
            if a==3:
                c.move(s,25,0)
                c.itemconfig(s,fill="brown")
                root.update()
                root.after(500)
            if a==4:
                c.move(s,25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            if a==5:
                c.move(s,25,0)
                c.itemconfig(s,fill="green")
                root.update()
                root.after(500)
            if a==6:
                c.move(s,25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            if a==7:
                c.move(s,25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            a=a+1
        else :
            if b==1:
                c.move(s,-25,0)
                c.itemconfig(s,fill="orange")
                root.update()
                root.after(500)
            if b==2:
                c.move(s,-25,0)
                c.itemconfig(s,fill="red")
                root.update()
                root.after(500)
            if b==3:
                c.move(s,-25,0)
                c.itemconfig(s,fill="brown")
                root.update()
                root.after(500)
            if b==4:
                c.move(s,-25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            if b==5:
                c.move(s,-25,0)
                c.itemconfig(s,fill="green")
                root.update()
                root.after(500)
            if b==6:
                c.move(s,-25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            b=b+1

    print(a)
    print(b)
    if(a>b):
        c.destroy()
        w=500
        h=500
        canvas = Canvas(root, width=w, height=h)
        canvas.pack()

        my_image = PhotoImage(file="bingo.ppm")
        my_img = canvas.create_image(0,0, anchor=NW, image=my_image)


        for x in range(0,60):
            canvas.move(my_img, 5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, 5)
    
            root.update()
            time.sleep(0.05)
    
        for x in range(0,60):
            canvas.move(my_img, -5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, -5)
            root.update()
            time.sleep(0.05)
    else:
        c.destroy()
        w=500
        h=500
        canvas = Canvas(root, width=w, height=h)
        canvas.pack()

        my_image = PhotoImage(file="loser.ppm")
        my_img = canvas.create_image(0,0, anchor=NW, image=my_image)


        for x in range(0,60):
            canvas.move(my_img, 5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, 5)
    
            root.update()
            time.sleep(0.05)
    
        for x in range(0,60):
            canvas.move(my_img, -5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, -5)
            root.update()
            time.sleep(0.05)
################################################################


def main_screen2():
    win.withdraw()
    global win1
    win1=Toplevel(win)
    win1.withdraw()
    win1 = Tk(className="Game Window")
    win1.title("GUESS THE PLACE..")
    win.geometry("300x250")

    Label(win1,text="GUESS THE PLACE..!!",width="50", height="2", font=("Arial Bold",25)).pack()  
    Label(win1,text="Welcome to The Game..",width="50", height="4", font=("Calibri",20)).pack(padx=4,pady=5)  
    Button(win1,text="START GAME", height="3", width="13",command=actp).pack()

def actp():
    win1.withdraw()
    global addimg1
    addimg1 = Toplevel(win)
    addimg1.title("GAME")
    addimg1.geometry("300x250")

    L1 = Label(addimg1,text = "1.Guess which place it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg1,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="amalficoast.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v=IntVar()
    def clicked():
        
        
        if v.get() == 1:
            L2 = Label(addimg1,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg1,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

        if v.get()==1:
            result.append(1)
        else:
            result.append(0)
    
         

    r1=Radiobutton(addimg1, text="malfi coast",padx=20,variable=v,value=4,command=clicked).pack(anchor=tk.W)
    r2=Radiobutton(addimg1, text="mama coast",padx=20,variable=v,value=2,command=clicked).pack(anchor=tk.W)
    r3=Radiobutton(addimg1, text="mafia coast",padx=20,variable=v,value=3,command=clicked).pack(anchor=tk.W)    
    r4=Radiobutton(addimg1, text="amalfi coast",padx=20,variable=v,value=1,command=clicked).pack(anchor=tk.W)
    
 
        
    Button(addimg1, text="NEXT", width=10, height=1,command=actp2).pack()


def actp2():
    addimg1.destroy()
    global addimg2
    addimg2 = Toplevel(win)
    addimg2.title("GAME")
    addimg2.geometry("300x250")

    L1 = Label(addimg2,text = "2.Guess which place it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg2,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="barcelonaspain.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v2=IntVar()
    def clicked2():
        
        
        if v2.get() == 1:
            L2 = Label(addimg2,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg2,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

        if v2.get()==1:
            result.append(1)
        else:
            result.append(0)
   
    
    v2=tk.IntVar()
    Radiobutton(addimg2, text="barbeque spain",padx=20,variable=v2,value=2,command=clicked2).pack(anchor=tk.W)
    Radiobutton(addimg2, text="barcelona spain",padx=20,variable=v2,value=1,command=clicked2).pack(anchor=tk.W)
    Radiobutton(addimg2, text="barce spain",padx=20,variable=v2,value=3,command=clicked2).pack(anchor=tk.W)    
    Radiobutton(addimg2, text="barcelona italy",padx=20,variable=v2,value=4,command=clicked2).pack(anchor=tk.W)
    
    
        
    Button(addimg2, text="NEXT", width=10, height=1,command=actp3).pack()


def actp3():
    addimg2.destroy()
    global addimg3
    addimg3 = Toplevel(win)
    addimg3.title("GAME")
    addimg3.geometry("300x250")

    L1 = Label(addimg3,text = "3.Guess which place it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg3,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="newyork.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v3=IntVar()
    def clicked3():
        
        
        if v3.get() == 1:
            L2 = Label(addimg3,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg3,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

        if v3.get()==1:
            result.append(1)
        else:
            result.append(0)
    
   
    Radiobutton(addimg3, text="new york",padx=20,variable=v3,value=1,command=clicked3).pack(anchor=tk.W)
    Radiobutton(addimg3, text="russia ",padx=20,variable=v3,value=2,command=clicked3).pack(anchor=tk.W)
    Radiobutton(addimg3, text="london",padx=20,variable=v3,value=3,command=clicked3).pack(anchor=tk.W)    
    Radiobutton(addimg3, text="france",padx=20,variable=v3,value=4,command=clicked3).pack(anchor=tk.W)

        
    Button(addimg3, text="NEXT", width=10, height=1,command=actp4).pack()


def actp4():
    addimg3.destroy()
    global addimg4
    addimg4 = Toplevel(win)
    addimg4.title("GAME")
    addimg4.geometry("300x250")

    L1 = Label(addimg4,text = "4.Guess which place it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg4,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="machupichu.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v4=IntVar()
    def clicked4():
        
        
        if v4.get() == 1:
            L2 = Label(addimg4,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg4,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

            
        if v4.get()==1:
            result.append(1)
        else:
            result.append(0)
   
    Radiobutton(addimg4, text="mauchi pu",padx=20,variable=v4,value=3,command=clicked4).pack(anchor=tk.W)
    Radiobutton(addimg4, text="machu",padx=20,variable=v4,value=2,command=clicked4).pack(anchor=tk.W)
    Radiobutton(addimg4, text="machupichu",padx=20,variable=v4,value=1,command=clicked4).pack(anchor=tk.W)    
    Radiobutton(addimg4, text="maldives",padx=20,variable=v4,value=4,command=clicked4).pack(anchor=tk.W)
    

        
    Button(addimg4, text="NEXT", width=10, height=1,command=actp5).pack()


def actp5():
    addimg4.destroy()
    global addimg5
    addimg5 = Toplevel(win)
    addimg5.title("GAME")
    addimg5.geometry("300x250")

    L1 = Label(addimg5,text = "5.Guess which place it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg5,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="riodejanerio.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v5=IntVar()
    def clicked5():
        
        
        if v5.get() == 1:
            L2 = Label(addimg5,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg5,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()
   
        if v5.get()==1:
            result.append(1)
        else:
            result.append(0)
    
    Radiobutton(addimg5, text="rio de janerio",padx=20,variable=v5,value=1,command=clicked5).pack(anchor=tk.W)
    Radiobutton(addimg5, text="las vegas",padx=20,variable=v5,value=2,command=clicked5).pack(anchor=tk.W)
    Radiobutton(addimg5, text="statue of liberity",padx=20,variable=v5,value=3,command=clicked5).pack(anchor=tk.W)    
    Radiobutton(addimg5, text="greece",padx=20,variable=v5,value=4,command=clicked5).pack(anchor=tk.W)

  
        
    Button(addimg5, text="NEXT", width=10, height=1,command=actp6).pack()


    
    
    
    
    
     
    
def actp6():
    addimg5.destroy()
    global addimg6
    addimg6 = Toplevel(win)
    addimg6.title("Game")
    addimg6.geometry("350x200")

    
    
    L2 = Label(addimg6,text = "6.Guess which place it is..??",width="50", height="3", font=("Calibri",13))
    L2.pack()
    canvas1=Canvas(addimg6,width=300, height=300)
    canvas1.pack()
    img1=PhotoImage(file="colosseum.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v6=IntVar()
    def clicked6():
        
        
        if v6.get() == 1:
            L2 = Label(addimg6,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg6,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()


        if v6.get()==1:
            result.append(1)
        else:
            result.append(0)


     
    Radiobutton(addimg6, text="paris",padx=20,variable=v6,value=4,command=clicked6).pack(anchor=tk.W)
    Radiobutton(addimg6, text="italy",padx=20,variable=v6,value=2,command=clicked6).pack(anchor=tk.W)
    Radiobutton(addimg6, text="qutub minar",padx=20,variable=v6,value=3,command=clicked6).pack(anchor=tk.W)    
    Radiobutton(addimg6, text="colosseum",padx=20,variable=v6,value=1,command=clicked6).pack(anchor=tk.W)    
    Button(addimg6, text="NEXT", width=10, height=1,command=actp7).pack()

    


def actp7():
    addimg6.destroy()
    global addimg7
    addimg7 = Toplevel(win)
    addimg7.title("Game")
    addimg7.geometry("350x200")

    L2 = Label(addimg7,text = "7.Guess which place it is..??",width="50", height="3", font=("Calibri",13))
    L2.pack()
    canvas1=Canvas(addimg7,width=300, height=300)
    canvas1.pack()
    img1=PhotoImage(file="tajmahal.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v7=IntVar()
    def clicked7():
        
        
        if v7.get() == 1:
            L2 = Label(addimg7,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg7,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()


        if v7.get()==1:
            result.append(1)
        else:
            result.append(0)


     
    Radiobutton(addimg7, text="white house",padx=20,variable=v7,value=3,command=clicked7).pack(anchor=tk.W)
    Radiobutton(addimg7, text="mecca",padx=20,variable=v7,value=2,command=clicked7).pack(anchor=tk.W)
    Radiobutton(addimg7, text="taj mahal",padx=20,variable=v7,value=1,command=clicked7).pack(anchor=tk.W)    
    Radiobutton(addimg7, text="royal pavillion",padx=20,variable=v7,value=4,command=clicked7).pack(anchor=tk.W)    
    Button(addimg7, text="NEXT", width=10, height=1,command=scorep).pack()

def scorep():
    win.destroy()
    root=Tk()
    c=Canvas(root,width=500,height=500,bg="black")
    s=c.create_oval(200,200,300,300,fill="yellow")
    cr=c.create_polygon(500,50,460,50,460,500,500,500,fill="green")
    t=0
    for i in range(9):
        cr=c.create_polygon(0,50+t,0,100+t,50,75+t,fill="red")
        t=t+50
    c.pack()
    a=1
    b=1
    print(result)
    for i in result:
        if i==1:
            if a==1:
                c.move(s,25,0)
                c.itemconfig(s,fill="orange")
                root.update()
                root.after(500)
            if a==2:
                c.move(s,25,0)
                c.itemconfig(s,fill="red")
                root.update()
                root.after(500)
            if a==3:
                c.move(s,25,0)
                c.itemconfig(s,fill="brown")
                root.update()
                root.after(500)
            if a==4:
                c.move(s,25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            if a==5:
                c.move(s,25,0)
                c.itemconfig(s,fill="green")
                root.update()
                root.after(500)
            if a==6:
                c.move(s,25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            if a==7:
                c.move(s,25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            a=a+1
        else :
            if b==1:
                c.move(s,-25,0)
                c.itemconfig(s,fill="orange")
                root.update()
                root.after(500)
            if b==2:
                c.move(s,-25,0)
                c.itemconfig(s,fill="red")
                root.update()
                root.after(500)
            if b==3:
                c.move(s,-25,0)
                c.itemconfig(s,fill="brown")
                root.update()
                root.after(500)
            if b==4:
                c.move(s,-25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            if b==5:
                c.move(s,-25,0)
                c.itemconfig(s,fill="green")
                root.update()
                root.after(500)
            if b==6:
                c.move(s,-25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            b=b+1

    print(a)
    print(b)
    if(a>b):
        c.destroy()
        w=500
        h=500
        canvas = Canvas(root, width=w, height=h)
        canvas.pack()

        my_image = PhotoImage(file="bingo.ppm")
        my_img = canvas.create_image(0,0, anchor=NW, image=my_image)


        for x in range(0,60):
            canvas.move(my_img, 5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, 5)
    
            root.update()
            time.sleep(0.05)
    
        for x in range(0,60):
            canvas.move(my_img, -5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, -5)
            root.update()
            time.sleep(0.05)
    else:
        c.destroy()
        w=500
        h=500
        canvas = Canvas(root, width=w, height=h)
        canvas.pack()

        my_image = PhotoImage(file="loser.ppm")
        my_img = canvas.create_image(0,0, anchor=NW, image=my_image)


        for x in range(0,60):
            canvas.move(my_img, 5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, 5)
    
            root.update()
            time.sleep(0.05)
    
        for x in range(0,60):
            canvas.move(my_img, -5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, -5)
            root.update()
            time.sleep(0.05)


######################################################################
    
    
          
def main_screen3():
    win.withdraw()
    global win1
    win1=Toplevel(win)
    win1.withdraw()
    win1 = Tk(className="Game Window")
    win1.title("GUESS THE MOVIE..")
    win1.geometry("300x250")

    Label(win1,text="GUESS THE MOVIE..!!",width="50", height="2", font=("Arial Bold",25)).pack()  
    Label(win1,text="Welcome to The Game..",width="50", height="4", font=("Calibri",20)).pack(padx=4,pady=5)  
    Button(win1,text="START GAME", height="3", width="13",command=actm).pack()

def actm():
    win1.withdraw()
    global addimg1
    addimg1 = Toplevel(win)
    addimg1.title("GAME")
    addimg1.geometry("300x250")

    L1 = Label(addimg1,text = "1.Guess which movie it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg1,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="IMAGE1.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v=IntVar()
    def clicked():
        
        
        if v.get() == 1:
            L2 = Label(addimg1,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg1,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

        if v.get()==1:
            result.append(1)
        else:
            result.append(0)
    
         

    r1=Radiobutton(addimg1, text="DDLJ",padx=20,variable=v,value=1,command=clicked).pack(anchor=tk.W)
    r2=Radiobutton(addimg1, text="KUCH KUCH HOTA HAI",padx=20,variable=v,value=2,command=clicked).pack(anchor=tk.W)
    r3=Radiobutton(addimg1, text="ISHQ",padx=20,variable=v,value=3,command=clicked).pack(anchor=tk.W)    
    r4=Radiobutton(addimg1, text="DILWALE",padx=20,variable=v,value=4,command=clicked).pack(anchor=tk.W)
    
 
        
    Button(addimg1, text="NEXT", width=10, height=1,command=act2m).pack()


def act2m():
    addimg1.destroy()
    global addimg2
    addimg2 = Toplevel(win)
    addimg2.title("GAME")
    addimg2.geometry("300x250")

    L1 = Label(addimg2,text = "2.Guess which movie it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg2,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="IMAGE2.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v2=IntVar()
    def clicked2():
        
        
        if v2.get() == 1:
            L2 = Label(addimg2,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg2,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

        if v2.get()==1:
            result.append(1)
        else:
            result.append(0)
   
    
    v2=tk.IntVar()
    Radiobutton(addimg2, text="DABANG",padx=20,variable=v2,value=1,command=clicked2).pack(anchor=tk.W)
    Radiobutton(addimg2, text="BAJRANGI BHAIJAAN",padx=20,variable=v2,value=2,command=clicked2).pack(anchor=tk.W)
    Radiobutton(addimg2, text="HELLO BROTHER",padx=20,variable=v2,value=3,command=clicked2).pack(anchor=tk.W)    
    Radiobutton(addimg2, text="DABANG 2",padx=20,variable=v2,value=4,command=clicked2).pack(anchor=tk.W)
    
    
        
    Button(addimg2, text="NEXT", width=10, height=1,command=act3m).pack()


def act3m():
    addimg2.destroy()
    global addimg3
    addimg3 = Toplevel(win)
    addimg3.title("GAME")
    addimg3.geometry("300x250")

    L1 = Label(addimg3,text = "3.Guess which movie it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg3,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="IMAGE3.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v3=IntVar()
    def clicked3():
        
        
        if v3.get() == 1:
            L2 = Label(addimg3,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg3,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

        if v3.get()==1:
            result.append(1)
        else:
            result.append(0)
    
   
    Radiobutton(addimg3, text="PADMAVAT",padx=20,variable=v3,value=1,command=clicked3).pack(anchor=tk.W)
    Radiobutton(addimg3, text="BAJIRAO MASTANI ",padx=20,variable=v3,value=2,command=clicked3).pack(anchor=tk.W)
    Radiobutton(addimg3, text="RAMLEELA",padx=20,variable=v3,value=3,command=clicked3).pack(anchor=tk.W)    
    Radiobutton(addimg3, text="MANIKARNIKA",padx=20,variable=v3,value=4,command=clicked3).pack(anchor=tk.W)

        
    Button(addimg3, text="NEXT", width=10, height=1,command=act4m).pack()


def act4m():
    addimg3.destroy()
    global addimg4
    addimg4 = Toplevel(win)
    addimg4.title("GAME")
    addimg4.geometry("300x250")

    L1 = Label(addimg4,text = "4.Guess which movie it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg4,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="IMAGE4.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v4=IntVar()
    def clicked4():
        
        
        if v4.get() == 1:
            L2 = Label(addimg4,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg4,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()

            
        if v4.get()==1:
            result.append(1)
        else:
            result.append(0)
   
    Radiobutton(addimg4, text="SOHNI MEHWAL",padx=20,variable=v4,value=1,command=clicked4).pack(anchor=tk.W)
    Radiobutton(addimg4, text="DAMINI",padx=20,variable=v4,value=2,command=clicked4).pack(anchor=tk.W)
    Radiobutton(addimg4, text="GHATAK",padx=20,variable=v4,value=3,command=clicked4).pack(anchor=tk.W)    
    Radiobutton(addimg4, text="JEET",padx=20,variable=v4,value=4,command=clicked4).pack(anchor=tk.W)
    

        
    Button(addimg4, text="NEXT", width=10, height=1,command=act5m).pack()


def act5m():
    addimg4.destroy()
    global addimg5
    addimg5 = Toplevel(win)
    addimg5.title("GAME")
    addimg5.geometry("300x250")

    L1 = Label(addimg5,text = "5.Guess which movie it is..??",width="50", height="3", font=("Calibri",13))
    L1.pack()
    canvas1=Canvas(addimg5,width=300,height=300)
    canvas1.pack()
    img1=PhotoImage(file="IMAGE5.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v5=IntVar()
    def clicked5():
        
        
        if v5.get() == 1:
            L2 = Label(addimg5,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg5,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()
   
        if v5.get()==1:
            result.append(1)
        else:
            result.append(0)
    
    Radiobutton(addimg5, text="KUCH KUCH HOTA HAI",padx=20,variable=v5,value=1,command=clicked5).pack(anchor=tk.W)
    Radiobutton(addimg5, text="DIL TO PAGAL HAI",padx=20,variable=v5,value=2,command=clicked5).pack(anchor=tk.W)
    Radiobutton(addimg5, text="MOHABBATEIN",padx=20,variable=v5,value=3,command=clicked5).pack(anchor=tk.W)    
    Radiobutton(addimg5, text="DILWALE",padx=20,variable=v5,value=4,command=clicked5).pack(anchor=tk.W)

  
        
    Button(addimg5, text="NEXT", width=10, height=1,command=act6m).pack()


    
    
    
    
    
     
    
def act6m():
    addimg5.destroy()
    global addimg6
    addimg6 = Toplevel(win)
    addimg6.title("Game")
    addimg6.geometry("350x200")

    
    
    L2 = Label(addimg6,text = "6.Guess which movie it is..??",width="50", height="3", font=("Calibri",13))
    L2.pack()
    canvas1=Canvas(addimg6,width=300, height=300)
    canvas1.pack()
    img1=PhotoImage(file="IMAGE6.ppm")
    canvas1.create_image(20,20,anchor=NW,image=img1)
    canvas1.image=img1
    canvas1.pack()
    v6=IntVar()
    def clicked6():
        
        
        if v6.get() == 1:
            L2 = Label(addimg6,text = "RIGHT ANSWER",width="50", height="3", font=("Calibri",13))
            L2.pack()
        else:
          L3 = Label(addimg6,text = "WRONG ANSWER",width="50", height="3", font=("Calibri",13))
          L3.pack()


        if v6.get()==1:
            result.append(1)
        else:
            result.append(0)


     
    Radiobutton(addimg6, text="SHOLAY",padx=20,variable=v6,value=1,command=clicked6).pack(anchor=tk.W)
    Radiobutton(addimg6, text="SHOLA AUR SHABNAM",padx=20,variable=v6,value=2,command=clicked6).pack(anchor=tk.W)
    Radiobutton(addimg6, text="YARANA",padx=20,variable=v6,value=3,command=clicked6).pack(anchor=tk.W)    
    Radiobutton(addimg6, text="MARD",padx=20,variable=v6,value=4,command=clicked6).pack(anchor=tk.W)    
    Button(addimg6, text="SHOW RESULT", width=10, height=1,command=scorem).pack()


def scorem():
    win.destroy()
    root=Tk()
    c=Canvas(root,width=500,height=500,bg="black")
    s=c.create_oval(200,200,300,300,fill="yellow")
    cr=c.create_polygon(500,50,460,50,460,500,500,500,fill="green")
    t=0
    for i in range(9):
        cr=c.create_polygon(0,50+t,0,100+t,50,75+t,fill="red")
        t=t+50
    c.pack()
    a=1
    b=1
    print(result)
    for i in result:
        if i==1:
            if a==1:
                c.move(s,25,0)
                c.itemconfig(s,fill="orange")
                root.update()
                root.after(500)
            if a==2:
                c.move(s,25,0)
                c.itemconfig(s,fill="red")
                root.update()
                root.after(500)
            if a==3:
                c.move(s,25,0)
                c.itemconfig(s,fill="brown")
                root.update()
                root.after(500)
            if a==4:
                c.move(s,25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            if a==5:
                c.move(s,25,0)
                c.itemconfig(s,fill="green")
                root.update()
                root.after(500)
            if a==6:
                c.move(s,25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            if a==7:
                c.move(s,25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            a=a+1
        else :
            if b==1:
                c.move(s,-25,0)
                c.itemconfig(s,fill="orange")
                root.update()
                root.after(500)
            if b==2:
                c.move(s,-25,0)
                c.itemconfig(s,fill="red")
                root.update()
                root.after(500)
            if b==3:
                c.move(s,-25,0)
                c.itemconfig(s,fill="brown")
                root.update()
                root.after(500)
            if b==4:
                c.move(s,-25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            if b==5:
                c.move(s,-25,0)
                c.itemconfig(s,fill="green")
                root.update()
                root.after(500)
            if b==6:
                c.move(s,-25,0)
                c.itemconfig(s,fill="blue")
                root.update()
                root.after(500)
            b=b+1

    print(a)
    print(b)
    if(a>b or a==b):
        c.destroy()
        w=500
        h=500
        canvas = Canvas(root, width=w, height=h)
        canvas.pack()

        my_image = PhotoImage(file="bingo.ppm")
        my_img = canvas.create_image(0,0, anchor=NW, image=my_image)


        for x in range(0,60):
            canvas.move(my_img, 5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, 5)
    
            root.update()
            time.sleep(0.05)
    
        for x in range(0,60):
            canvas.move(my_img, -5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, -5)
            root.update()
            time.sleep(0.05)
    else:
        c.destroy()
        w=500
        h=500
        canvas = Canvas(root, width=w, height=h)
        canvas.pack()

        my_image = PhotoImage(file="loser.ppm")
        my_img = canvas.create_image(0,0, anchor=NW, image=my_image)


        for x in range(0,60):
            canvas.move(my_img, 5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, 5)
    
            root.update()
            time.sleep(0.05)
    
        for x in range(0,60):
            canvas.move(my_img, -5, 0)
            root.update()
            time.sleep(0.05)

        for x in range(0,60):
            canvas.move(my_img, 0, -5)
            root.update()
            time.sleep(0.05)






 


Button(win,text="LOGOS", height="3", width="13",command=main_screen1).pack()
Button(win,text="PLACES", height="3", width="13",command=main_screen2).pack()
Button(win,text="MOVIES", height="3", width="13",command=main_screen3).pack()

win.mainloop()

