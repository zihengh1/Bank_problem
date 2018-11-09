import random
import time

random.seed(time)
resource_num = random.randint(2, 5)
custumer_num = random.randint(2, 6)
allocation = []
Max = []
for i in range(custumer_num):
    allocation.append(random.sample(range(1, 8), resource_num))
    Max.append(random.sample(range(8, 14), resource_num))

Bank_Avaliable = random.sample(range(2, 7), resource_num)

