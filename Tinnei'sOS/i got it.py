from tkinter import *
import time
 
num = 1
 
tk = Tk()
tk.geometry('893x777')
canvas = Canvas(tk,height=777, width=893)
image_file = PhotoImage(file="background.gif")
image = canvas.create_image(446.5, 0, anchor='n',image=image_file)

canvas.pack()

while(1): 
    num = num +1
    itext = canvas.create_text(583, 415, text = num, fill = 'black' ,font=('Arial',18))
    print('num=%s' %num)
    itext = canvas.create_text(590, 449, text = num, fill = 'black' ,font=('Arial',18))
    tk.update()
    print('num=%s' %num)
    rect = canvas.create_rectangle(563, 395, 603, 435, fill = 'light gray', outline="")
    rect = canvas.create_rectangle(570, 429, 610, 469, fill = 'light gray', outline="")
    tk.after(1000)
 


