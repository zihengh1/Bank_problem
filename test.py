from tkinter import *
import random
import time

def stop():
    print("stop")

def take_back_resource(c, alloc, cur_t):
    msg = "Finish, Return Bank money"
    cur_t = list(map(lambda x: x[0] + x[1], list(zip(alloc, cur_t))))
    return cur_t, msg

def determine_state(i, cus, total):
    state = 1 # Safe
    for c, t in zip(cus, total):
        if c > t:
            state = 0 # Unsafe
            msg = "Unsafe, " + name_data[i] + " Please wait in Line again"
            return state, msg
    msg = "Safe, Lend " + name_data[i] + " money"
    return state, msg

def initial_need(Max, alloc):
    Need = []
    for M, a in zip(Max, alloc):
        n = list(map(lambda x: x[0] - x[1], list(zip(M, a))))
        Need.append(n)
    return Need

# define every parameter 
random.seed(time)
resource_num = 3
customer_n = 4
customer_list = [x for x in range(customer_n)]
alloc = []
Max = []
name_data = ['Anna', 'Zoe', 'Tina', 'Joe']
picture = []

for i in range(customer_n):
    alloc.append([])
    Max.append([])
    for j in range(resource_num):
        tmp = random.randint(0, 3)
        alloc[i].append(tmp)
        Max[i].append(random.randint(3, 6))
current_total = random.sample(range(3, 6), resource_num)

# caculate customer need
Need = initial_need(Max, alloc)
print("Max", Max)
print("Alloc", alloc)
print("Need", Need)    

# deadlock counter
count = 0
is_safe = 0
current_cus_num = customer_n
round_num = 0
message = []

window = Tk()

# named the window 
window.title('OS Bank')

# window size
window.geometry('890x750')

# canvas 
canvas = Canvas(window,height=700, width=890)

# load the picture
image_file = PhotoImage(file="./Back_ground.png")

# picture position
image = canvas.create_image(446.5, 0, anchor='n',image=image_file)


# Create a button
button = Button(window, text='New Program Start', font=('Arial', 18), width=30, height=3, command=stop)
button.pack()

while(len(customer_list)):
    print("round_num", round_num)
    dead = 0
    customer_id = customer_list[0]
    # Text Position
    if round_num:
        name = canvas.create_text(240, 250, text = name_data[customer_id], fill = 'black', font=('Arial',25))
        
    JPY = canvas.create_text(560, 170, text = current_total[0], fill = 'black', font=('Arial',25))
    TWD = canvas.create_text(560, 205, text = current_total[1], fill = 'black', font=('Arial',25))
    CNY = canvas.create_text(560, 235, text = current_total[2], fill = 'black', font=('Arial',25))
    
    # Alloc / Need / Max
    P1R1 = canvas.create_text(215, 475, text = str(alloc[0][0]) + " / " + str(Need[0][0]) + " / " + str(Max[0][0]), \
                              fill = 'black', font=('Arial',16))
    P1R2 = canvas.create_text(290, 475, text = str(alloc[0][1]) + " / " + str(Need[0][1]) + " / " + str(Max[0][1]), \
                              fill = 'black', font=('Arial',16))
    P1R3 = canvas.create_text(365, 475, text = str(alloc[0][2]) + " / " + str(Need[0][2]) + " / " + str(Max[0][2]), \
                              fill = 'black', font=('Arial',16))
    
    P2R1 = canvas.create_text(215, 525, text = str(alloc[1][0]) + " / " + str(Need[1][0]) + " / " + str(Max[1][0]), \
                              fill = 'black', font=('Arial',16))
    P2R2 = canvas.create_text(290, 525, text = str(alloc[1][1]) + " / " + str(Need[1][1]) + " / " + str(Max[1][1]), \
                              fill = 'black', font=('Arial',16))
    P2R3 = canvas.create_text(365, 525, text = str(alloc[1][2]) + " / " + str(Need[1][2]) + " / " + str(Max[1][2]), \
                              fill = 'black', font=('Arial',16)) 
    
    P3R1 = canvas.create_text(215, 585, text = str(alloc[2][0]) + " / " + str(Need[2][0]) + " / " + str(Max[2][0]), \
                              fill = 'black', font=('Arial',16))
    P3R2 = canvas.create_text(290, 585, text = str(alloc[2][1]) + " / " + str(Need[2][1]) + " / " + str(Max[2][1]), \
                              fill = 'black', font=('Arial',16))
    P3R3 = canvas.create_text(365, 585, text = str(alloc[2][2]) + " / " + str(Need[2][2]) + " / " + str(Max[2][2]), \
                              fill = 'black', font=('Arial',16))
    
    P4R1 = canvas.create_text(215, 645, text = str(alloc[3][0]) + " / " + str(Need[3][0]) + " / " + str(Max[3][0]), \
                              fill = 'black', font=('Arial',16))
    P4R2 = canvas.create_text(290, 645, text = str(alloc[3][1]) + " / " + str(Need[3][1]) + " / " + str(Max[3][1]), \
                              fill = 'black', font=('Arial',16))
    P4R3 = canvas.create_text(365, 645, text = str(alloc[3][2]) + " / " + str(Need[3][2]) + " / " + str(Max[3][2]), \
                              fill = 'black', font=('Arial',16))
    
    if round_num:
        message_text = canvas.create_text(650, 290 + (round_num) * 60, text = "Bank: " + message[2 * round_num - 2], \
                                          fill = 'black', font=('Arial',18))
        message_text = canvas.create_text(650, 320 + (round_num) * 60, text = message[2 * round_num - 1], \
                                          fill = 'black', font=('Arial',18))
    window.update()

    # erase 
    if round_num:
        name_erase = canvas.create_rectangle(200, 230, 285, 280, fill = 'light gray', outline="")
        
    JPY_erase = canvas.create_rectangle(545, 160, 575, 180, fill = 'light gray', outline="")
    TWD_erase = canvas.create_rectangle(545, 195, 575, 215, fill = 'light gray', outline="")
    CNY_erase = canvas.create_rectangle(545, 225, 575, 245, fill = 'light gray', outline="")
    
    P1R1_erase = canvas.create_rectangle(185, 455, 240, 490, fill = 'gray92', outline="")
    P1R2_erase = canvas.create_rectangle(260, 455, 315, 490, fill = 'gray92', outline="")
    P1R3_erase = canvas.create_rectangle(335, 455, 390, 490, fill = 'gray92', outline="")
    
    P2R1_erase = canvas.create_rectangle(185, 515, 240, 550, fill = 'gray92', outline="")
    P2R2_erase = canvas.create_rectangle(260, 515, 315, 550, fill = 'gray92', outline="")
    P2R3_erase = canvas.create_rectangle(335, 515, 390, 550, fill = 'gray92', outline="")
    
    P3R1_erase = canvas.create_rectangle(185, 575, 240, 610, fill = 'gray92', outline="")
    P3R2_erase = canvas.create_rectangle(260, 575, 315, 610, fill = 'gray92', outline="")
    P3R3_erase = canvas.create_rectangle(335, 575, 390, 610, fill = 'gray92', outline="")
    
    P4R1_erase = canvas.create_rectangle(185, 635, 240, 665, fill = 'gray92', outline="")
    P4R2_erase = canvas.create_rectangle(260, 635, 315, 665, fill = 'gray92', outline="")
    P4R3_erase = canvas.create_rectangle(335, 635, 390, 665, fill = 'gray92', outline="")

    window.after(1000)
    canvas.pack()
    
    # deadlock statement
    if(is_safe == 1):
        count = 0
    if(count == current_cus_num):
        dead = 1
        break
        
    s, msg1 = determine_state(customer_id, Need[customer_id], current_total)
    print(msg1)
    message.append(msg1)
    if(s):
        # use_my_money(customer_id)
        # alloc = max and need = 0
        current_total, msg2 = take_back_resource(customer_id, alloc[customer_id], current_total)
        print(msg2)
        message.append(msg2)
        alloc[customer_id] = [0, 0, 0]
        Need[customer_id] = [0, 0, 0]
        current_cus_num = current_cus_num - 1
        is_safe = 1
    else:
        message.append("Won't Lend " + name_data[customer_id] + " money")
        customer_list.append(customer_id)
        count = count + 1
        is_safe = 0
        
    customer_list.pop(0)    
    print("Current bank money: ", current_total)
    print("Max", Max)
    print("Allocation", alloc)
    print("Need", Need)
    round_num = round_num + 1
    # print(message)
    time.sleep(2)

if(dead):
    print("DeadLock")
    game_text = canvas.create_text(650, 650, text = "DeadLock", fill = 'black', font=('Arial',25))
else:
    print("New program start")
    game_text = canvas.create_text(650, 650, text = "New program start", fill = 'black', font=('Arial',25))
    
canvas.mainloop()
