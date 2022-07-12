import random
import threading
import tkinter as tk
import time
import turtle as t
from turtle import *
import random as r

def createtree():
    n = 100.0
    speed("fastest")
    screensize(bg='black')
    left(90)
    forward(3 * n)
    color("orange", "yellow")
    begin_fill()
    left(126)
    for i in range(5):
        forward(n / 5)
        right(144)
        forward(n / 5)
        left(72)
    end_fill()
    right(126)

    def drawlight():
        if r.randint(0, 40) == 0:
            color('tomato')
            circle(5)
        elif r.randint(0, 35) == 1:
            color('orange')
            circle(3)
        else:
            color('dark green')

    color("dark green")
    backward(n * 4.8)

    def tree(d, s):
        if d <= 0: return
        forward(s)
        tree(d - 1, s * .8)
        right(120)
        tree(d - 3, s * .5)
        drawlight()
        right(120)
        tree(d - 3, s * .5)
        right(120)
        backward(s)

    tree(15, n)
    backward(n / 2)

    for i in range(200):
        a = 200 - 400 * r.random()
        b = 10 - 20 * r.random()
        up()
        forward(b)
        left(90)
        forward(a)
        down()
        if r.randint(0, 1) == 0:
            color('tomato')
        else:
            color('wheat')
        circle(2)
        up()
        backward(a)
        right(90)
        backward(b)

    t.color("dark red", "red")
    t.write("期末加油！If I can help just let me know", align="center", font=("Comic Sans MS", 25, "bold"))

    def drawsnow():
        t.ht()
        t.pensize(2)
        for i in range(200):
            t.pencolor("white")
            t.pu()
            t.setx(r.randint(-350, 350))
            t.sety(r.randint(-100, 350))
            t.pd()
            dens = 6
            snowsize = r.randint(1, 10)
            for j in range(dens):
                t.fd(int(snowsize))
                t.backward(int(snowsize))
                t.right(int(360 / dens))

    drawsnow()
    t.done()

def show1(b,B):
    b['text']='呃，本来想给你show个和端午节有关系的，\n但是它画的粽子是真的有点丑，，，\n这个的话感觉相对还算比较好看的那种了'
    b['command']=lambda :show2(b,B)
    b['font']=('华文行楷', 30)
    b['width']=38
    b['height']=10
    B['text']="（还是个按钮）"

def show2(b,B):
    b['text']='但是这个可能花的时间会比较久一点，\n你要耐心哦，（点我）'
    b['command']=createtree
    b['fg']='black'
    b['bg']='pink'
    B['text']="（但是这个程序可没有这么简单哈哈）"

def dow():
    t = tk.Tk()
    width = t.winfo_screenwidth()
    height = t.winfo_screenheight()
    a = random.randrange(0, width)
    b=random.randrange(0, height)
    t.title('')
    t.geometry('800x500' + '+' + str(a) + '+' + str(b))
    b=tk.Button(t, text='***~\n端午节快乐！',cursor='circle',font=('华文行楷', 50),fg='white', command=lambda :show1(b,B),bg='black',width=22,height=6)
    b.pack()
    B = tk.Label(t,text='（上面那个是个按钮）',font=10)
    B.pack()
    t.mainloop()
    for i in range(15):
        t = threading.Thread(target=dow)
        time.sleep(0.3)
        t.start()
dow()