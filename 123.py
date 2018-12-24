from tkinter import *
import time
import tkinter as tk
num = 0

# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('OS Bank')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('893x850')  # 这里的乘是小x
 
canvas = Canvas(window,height=777, width=893)
image_file = PhotoImage(file="background.gif")
image = canvas.create_image(446.5, 0, anchor='n',image=image_file)
canvas.pack()


def stop():
    global num
    num = 0
    

 
# 第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='Clear', font=('Arial', 12), width=10, height=1,command=stop)
b.pack()

while(1): 
    num = num +1
    #數字位置
    P1 = canvas.create_text(583, 415, text = num, fill = 'black' ,font=('Arial',18))
    print('num=%s' %num)
    #數字位置
    P2 = canvas.create_text(590, 449, text = num, fill = 'black' ,font=('Arial',18))
    window.update()
    print('num=%s' %num)
    #用一個正方形擋住，大小為40*40
    rect = canvas.create_rectangle(563, 395, 603, 435, fill = 'light gray', outline="")
    rect = canvas.create_rectangle(570, 429, 610, 469, fill = 'light gray', outline="")     
    window.after(1000)

