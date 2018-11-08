import config as cf
import time

def caculate_beed(Max, alloc):
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
            print("Unsafe")
            return state
    print("Safe")
    return state

def take_back_resource(alloc, cur_t):
    cur_t = list(map(lambda x: x[0] + x[1], list(zip(alloc, cur_t))))
    return cur_t

# define every parameter 
c_n = cf.custumer_num
c = [x for x in range(c_n)]
print(c)
alloc = cf.allocation
Max = cf.Max
current_total = cf.Bank_Avaliable
print("Cur_t: ", current_total)
# caculate costumer need
print("Max       Allocate  Need")
Need = caculate_beed(Max, alloc)

while(len(c) is not 0):
    dead = 0
    costumer = c[0]
    print("# NUM: ", costumer)
    print("waiting: ", c)
    if(determine_state(Need[costumer], current_total)):
        print("take back")
        current_total = take_back_resource(alloc[costumer], current_total)
    else:
        c.append(costumer)
    c.pop(0)    
    print("cur_total: ", current_total)
    time.sleep(3)

if(dead is 1):
    print("DeadLock")
else:
    print("New program start")
    
    

