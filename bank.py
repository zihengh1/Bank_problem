import config as cf
import time

def caculate_need(Max, alloc):
    Need = []
    for M, a in zip(Max, alloc):
        n = list(map(lambda x: x[0] - x[1], list(zip(M, a))))
        Need.append(n)
        print(M, a, n)
    return Need

def determine_state(cus, total):
    state = 1 # Safe
    for c, t in zip(cus, total):
        if c > t:
            state = 0 # Unsafe
            print("Unsafe, Please wait in Line again")
            return state
    print("Safe, Lend you money")
    return state

def take_back_resource(alloc, cur_t):
    print("Finish, Return my money")
    cur_t = list(map(lambda x: x[0] + x[1], list(zip(alloc, cur_t))))
    return cur_t

# define every parameter 
c_n = cf.costumer_num
c = [x for x in range(c_n)]
alloc = cf.allocation
Max = cf.Max
current_total = cf.Bank_Avaliable
print("Currrent bank money: ", current_total)

# caculate costumer need
print("Max||Allocate||Need")
Need = caculate_need(Max, alloc)

#deadlock counter
count = 0

is_safe = 0
current_cus_num = c_n

while(len(c) is not 0):
    
    #deadlock statement
    #if(count == current_cus_num+1):
        #dead = 1
        #break
   # if((is_safe == 0) & (count == current_cus_num)):
        #dead = 1
        #break

    if(is_safe == 0):
        if(count == current_cus_num):
            dead = 1
            break
    else:
        if(count == current_cus_num+1):
            dead = 1
            break

    print("test: ", current_cus_num, count, is_safe)
    dead = 0
    costumer = c[0]
    print("# NUM %d: %s" %(costumer,cf.name_data[costumer]))
    print("waiting queue: ", c)

    if(determine_state(Need[costumer], current_total)):
        current_total = take_back_resource(alloc[costumer], current_total)
        current_cus_num -= 1
        is_safe = 1

    else:
        c.append(costumer)
        count = count + 1

    c.pop(0)    
    print("Current bank money: ", current_total)
    time.sleep(3)
    
if(dead is 1):
    print("DeadLock")
else:
    print("New program start")
    
    

