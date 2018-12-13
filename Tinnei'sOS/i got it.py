from tkinter import *
import time
 
num = 1
 
tk = Tk()
#視窗取名字
tk.title('OS Bank')
#視窗大小
tk.geometry('893x777')
#畫布大小
canvas = Canvas(tk,height=777, width=893)
#載入圖片
image_file = PhotoImage(file="background.gif")
#圖片位置
image = canvas.create_image(446.5, 0, anchor='n',image=image_file)

canvas.pack()

while(1): 
    num = num +1
    #數字位置
    P1 = canvas.create_text(583, 415, text = num, fill = 'black' ,font=('Arial',18))
    print('num=%s' %num)
    #數字位置
    P2 = canvas.create_text(590, 449, text = num, fill = 'black' ,font=('Arial',18))
    tk.update()
    print('num=%s' %num)
    #用一個正方形擋住，大小為40*40
    rect = canvas.create_rectangle(563, 395, 603, 435, fill = 'light gray', outline="")
    rect = canvas.create_rectangle(570, 429, 610, 469, fill = 'light gray', outline="")
    tk.after(1000)
 



