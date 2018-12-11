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
#添加文本
text = canvas.create_text(580,189, text = 'A',fill = 'black' ,font=('Arial',18))
text = canvas.create_text(580,225, text = 'B',fill = 'black' ,font=('Arial',18))
text = canvas.create_text(580,260, text = 'C',fill = 'black' ,font=('Arial',18))

text = canvas.create_text(186,532, text = 'P1R1',fill = 'black' ,font=('Arial',16))
text = canvas.create_text(267,532, text = 'P1R2',fill = 'black' ,font=('Arial',16))
text = canvas.create_text(348,532, text = 'P1R3',fill = 'black' ,font=('Arial',16))
text = canvas.create_text(186,595, text = 'P2R1',fill = 'black' ,font=('Arial',16))
text = canvas.create_text(267,595, text = 'P2R2',fill = 'black' ,font=('Arial',16))
text = canvas.create_text(348,595, text = 'P2R3',fill = 'black' ,font=('Arial',16)) 
text = canvas.create_text(186,659, text = 'P3R1',fill = 'black' ,font=('Arial',16))
text = canvas.create_text(267,659, text = 'P3R2',fill = 'black' ,font=('Arial',16))
text = canvas.create_text(348,659, text = 'P3R3',fill = 'black' ,font=('Arial',16))
text = canvas.create_text(186,719, text = 'P4R1',fill = 'black' ,font=('Arial',16))
text = canvas.create_text(267,719, text = 'P4R2',fill = 'black' ,font=('Arial',16))
text = canvas.create_text(348,719, text = 'P4R3',fill = 'black' ,font=('Arial',16))

text = canvas.create_text(583,415, text = 'P1',fill = 'black' ,font=('Arial',18))
text = canvas.create_text(590,449, text = 'P2',fill = 'black' ,font=('Arial',18))
text = canvas.create_text(590,484, text = 'P2',fill = 'black' ,font=('Arial',18))
text = canvas.create_text(590,520, text = 'P3',fill = 'black' ,font=('Arial',18))
text = canvas.create_text(590,555, text = 'P4',fill = 'black' ,font=('Arial',18))
text = canvas.create_text(583,588, text = 'P1',fill = 'black' ,font=('Arial',18))


canvas.pack()
