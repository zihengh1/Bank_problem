import tkinter as tk  

window = tk.Tk()
 
#視窗取名字
window.title('OS Bank')
#視窗大小
window.geometry('893x777')
 
#canvas 畫布
canvas = tk.Canvas(window,height=777, width=893)
#載入圖片
image_file = tk.PhotoImage(file="background.gif")
#圖片位置
image = canvas.create_image(446.5, 0, anchor='n',image=image_file) 
canvas.pack()
