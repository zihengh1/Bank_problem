import random
import numpy as np
import time
import threading

def release_resource(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c

def safe_or_not(cus, tol):
    state = 1 
    for c, t in zip(cus, tol):
        if c > t:
            state = 0 # Unsafe
            msg = "Unsafe, Please wait in Line again"
            return state, msg
    msg = "Safe, Lend you money"
    return state, msg


class MyThread(threading.Thread):
    def __init__(self, num, name, alloc, Max, need, bank, lock):
        threading.Thread.__init__(self)

        self.num = num
        self.name = name
        self.alloc = alloc
        self.Max = Max
        self.need = need
        self.bank = bank
        self.lock = lock

    def run(self):
        lock.acquire()
        print("Customer %d, %s:" % (self.num, self.name))
        print("Bank_Current: %s" % (self.bank.get()))
        s, msg = safe_or_not(self.need, self.bank.get())
        print("Alloc: %s" % (self.alloc))
        print("Max: %s"% (self.Max))
        print(msg)

        if(s):
            deadlock_count = 1;
            tmp_arr = release_resource(self.alloc, self.bank.get())
            self.bank.set(tmp_arr)

        """
        else:
            #self.bank.add_unchange()
            #if((self.bank.get_unchange()) < 4):
            time.sleep(7)
            MyThread(self.num, self.name, self.alloc, self.Max, self.need, self.bank, self.lock).start()
            """

        self.lock.release()
        time.sleep(2)


class Bank:
    def __init__(self, total):
        self.total = total
        self.unchange = 0
    def get(self):
        return self.total
    def set(self, newtotal):
        self.total = newtotal
    """def add_unchange(self):
        self.unchange += 1
    def get_unchange(self):
        return self.unchange"""

# main code
init_bank = []
for i in range(3):
    n = random.randint(6, 9)
    init_bank.append(n)

bank = Bank(init_bank)
print("(Bank_initAlloc: %s)"% (bank.get()))

name_data = ['Anna', 'Zoe', 'Tina', 'Joe']
lock = threading.Lock()
threads = []
for i in range(4):
    alloc = []
    Max = []
    need = []
    name = name_data[i]

    for j in range(3):        
        x = random.randint(0, 3)
        y = random.randint(3, 6)
        alloc.append(x)
        Max.append(y)
        need.append(y - x)
    threads.append(MyThread(i, name, alloc, Max, need, bank, lock))
    threads[i].start()
    time.sleep(2)

for i in range(4):
    threads[i].join()

print("Done.")

