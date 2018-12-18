import config as cf
import time

def initial_need(Max, alloc):
    Need = []
    for M, a in zip(Max, alloc):
        n = list(map(lambda x: x[0] - x[1], list(zip(M, a))))
        Need.append(n)
    return Need

def determine_state(cus, total):
    state = 1 # Safe
    for c, t in zip(cus, total):
        if c > t:
            state = 0 # Unsafe
            msg = "Unsafe, Please wait in Line again"
            return state, msg
    msg = "Safe, Lend you money"
    return state, msg

def take_back_resource(alloc, cur_t):
    msg = "Finish, Return my money"
    cur_t = list(map(lambda x: x[0] + x[1], list(zip(alloc, cur_t))))
    return cur_t, msg

# define every parameter 
customer_n = cf.customer_num
customer_list = [x for x in range(customer_n)]
alloc = cf.allocation
Max = cf.Max
current_total = cf.Bank_Avaliable
print("Initial bank money: ", current_total)

# caculate customer need
Need = initial_need(Max, alloc)
# Max, alloc, Need

# deadlock counter
count = 0
is_safe = 0
current_cus_num = customer_n

while(len(customer_list) is not 0):
    # deadlock statement
    if(is_safe == 1):
        count = 0
    if(count == current_cus_num):
        dead = 1
        break

    dead = 0
    customer_now = customer_list[0]
    print("# NAME: %s" % (cf.name_data[customer_now]))
    print("waiting queue: ", customer_list)

    s, msg = determine_state(Need[customer_now], current_total)
    print(msg)
    if(s):
        current_total, msg = take_back_resource(alloc[customer_now], current_total)
        print(msg)
        current_cus_num = current_cus_num - 1
        is_safe = 1

    else:
        customer_list.append(customer_now)
        count = count + 1
        is_safe = 0

    customer_list.pop(0)    
    print("Current bank money: ", current_total)
    time.sleep(3)
    
if(dead is 1):
    print("DeadLock")
else:
    print("New program start")
        

