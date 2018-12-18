import random
import time

random.seed(time)
resource_num = 3
customer_num = 4
allocation = []
Max = []
name_data = ['Anna', 'Zoe', 'Tina', 'Joe']

for i in range(customer_num):
    allocation.append([])
    Max.append([])

    for j in range(resource_num):
        tmp = random.randint(0, 3)
        allocation[i].append(tmp)
        Max[i].append(random.randint(3, 6))

Bank_Avaliable = random.sample(range(3, 6), resource_num)
